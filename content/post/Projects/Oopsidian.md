---
title: Projects Oopsidian
date: 2024-12-20
---

## code of app.tsx with tailwind css

```typescript
// App.tsx

import React, { useState, useEffect } from 'react';

import ReactMarkdown from 'react-markdown';

import { PlusCircle, FileText, Save } from 'lucide-react';

import Chatbot from './Chatbot';

import NoteGraph from './NoteGraph'

import './App.css'

  

interface Note {

id: string;

title: string;

content: string;

links: string[];

lastModified: Date;

}

  

interface GraphData {

nodes: Array<{ id: string; name: string }>;

links: Array<{ source: string; target: string }>;

}

  

const App: React.FC = () => {

  

const [notes, setNotes] = useState<Note[]>(() => {

const savedNotes = localStorage.getItem('notes');

return savedNotes ? JSON.parse(savedNotes) : [];

});

const [currentNote, setCurrentNote] = useState<Note | null>(null);

const [graphData, setGraphData] = useState<GraphData>({ nodes: [], links: [] });

const [isDarkMode, setIsDarkMode] = useState(true);

  

// Save notes to localStorage whenever they change

useEffect(() => {

localStorage.setItem('notes', JSON.stringify(notes));

}, [notes]);

  

// Update graph data whenever notes change

useEffect(() => {

updateGraphData(notes);

}, [notes]);

  

const extractLinks = (content: string): string[] => {

const linkRegex = /\[\[(.*?)\]\]/g;

const matches = content.match(linkRegex) || [];

return matches.map(match => match.slice(2, -2));

};

  

const updateGraphData = (notesData: Note[]) => {

const nodes = notesData.map(note => ({

id: note.id,

name: note.title,

}));

  

const links: Array<{ source: string; target: string }> = [];

notesData.forEach(note => {

note.links.forEach(linkTitle => {

const targetNote = notesData.find(n => n.title === linkTitle);

if (targetNote) {

links.push({

source: note.id,

target: targetNote.id,

});

}

});

});

  

setGraphData({ nodes, links });

};

  

const createNewNote = () => {

  

const newNote: Note = {

id: Date.now().toString(),

title: 'Untitled Note',

content: '',

links: [],

lastModified: new Date(),

};

setNotes(prev => [...prev, newNote]);

setCurrentNote(newNote);

  
  
  

};

  

const updateNoteContent = (id: string, content: string) => {

  

setTimeout(() => {

window.scrollTo(0, 0);

}, 1);

  

const updatedNotes = notes.map(note => {

if (note.id === id) {

const links = extractLinks(content);

return { ...note, content, links, lastModified: new Date() };

}

return note;

});

setNotes(updatedNotes);

if (currentNote) {

setCurrentNote({ ...currentNote, content, lastModified: new Date() });

}

};

  

const updateNoteTitle = (id: string, title: string) => {

  
  

  

const updatedNotes = notes.map(note => {

if (note.id === id) {

return { ...note, title, lastModified: new Date() };

}

return note;

});

setNotes(updatedNotes);

if (currentNote) {

setCurrentNote({ ...currentNote, title, lastModified: new Date() });

}

};

  

const deleteNote = (id: string) => {

setNotes(notes.filter(note => note.id !== id));

if (currentNote?.id === id) {

setCurrentNote(null);

}

};

  

const toggleTheme = () => {

setIsDarkMode(!isDarkMode);

document.documentElement.classList.toggle('dark');

};

  

useEffect(()=>{

console.log("reend")

});

  

return (

<div className={`flex h-screen ${isDarkMode ? 'dark' : ''}`}>

{/* Sidebar */}

<div className="lg:w-64 w-16 bg-gray-100 dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 flex flex-col transition-all duration-300 ease-in-out">

{/* Sidebar Header */}

<div className="p-4 border-b border-gray-200 dark:border-gray-700">

<button

onClick={createNewNote}

className="w-full flex items-center justify-center gap-2 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg transition-colors"

>

<PlusCircle size={20} />

<span>New Note</span>

</button>

</div>

  

{/* Notes List */}

<div className="flex-1 overflow-y-auto">

{notes.map(note => (

<div

key={note.id}

onClick={() => {

  
  

setTimeout(() => {

window.scrollTo(0, 0);

}, 10);

setCurrentNote(note);

  

console.log("hi")

  

setTimeout(() => {

window.scrollTo(0, 0);

}, 10);

}

}

className={`flex items-center gap-2 p-3 cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors

${currentNote?.id === note.id ? 'bg-gray-200 dark:bg-gray-700' : ''}`}

>

<FileText size={18} className="text-gray-500 dark:text-gray-400" />

<div className="flex-1 min-w-0">

<div className="truncate text-gray-900 dark:text-gray-100">{note.title}</div>

<div className="text-xs text-gray-500 dark:text-gray-400">

{new Date(note.lastModified).toLocaleDateString()}

</div>

</div>

</div>

))}

</div>

  

{/* Theme Toggle */}

<div className="p-4 border-t border-gray-200 dark:border-gray-700">

<button

onClick={toggleTheme}

className="w-full py-2 px-4 rounded-lg bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200"

>

{isDarkMode ? '🌞 Light Mode' : '🌙 Dark Mode'}

</button>

</div>

</div>

  

{/* Main Content */}

<div className="flex-1 flex flex-col bg-white dark:bg-gray-900" >

{currentNote ? (

<div className="flex-1 flex">

{/* Editor */}

<div className="flex-1 flex flex-col p-4 border-r border-gray-200 dark:border-gray-700">

<input

type="text"

value={currentNote.title}

onChange={(e) => updateNoteTitle(currentNote.id, e.target.value)}

className="w-full mb-4 p-2 text-lg font-semibold bg-transparent border-b border-gray-200 dark:border-gray-700 text-gray-900 dark:text-gray-100 focus:outline-none focus:border-blue-500"

placeholder="Note Title"

/>

<textarea

style={{"height":"50vh"}}

value={currentNote.content}

onChange={(e) => updateNoteContent(currentNote.id, e.target.value)}

className="flex-1 w-full p-2 bg-transparent text-gray-900 dark:text-gray-100 focus:outline-none resize-none"

placeholder="Write your note here... Use [[Note Title]] to link to other notes."

/>

<div className="flex justify-between items-center pt-2 text-sm text-gray-500 dark:text-gray-400">

<div>

Last modified: {new Date(currentNote.lastModified).toLocaleString()}

</div>

<button

onClick={() => deleteNote(currentNote.id)}

className="text-red-500 hover:text-red-600 px-2 py-1 rounded"

>

Delete Note

</button>

</div>

</div>

  

{/* Preview */}

<div className="flex-1 p-4 overflow-auto bg-gray-50 dark:bg-gray-800" style={{"height":"50vh"}}>

<div className="prose dark:prose-invert max-w-none">

<ReactMarkdown>{currentNote.content}

  

  

</ReactMarkdown>

</div>

</div>

<div className="w-96">

<Chatbot noteTitle={currentNote.content} />

</div>

</div>

  
  
  

) : (

<div className="flex-1 flex items-center justify-center text-gray-500 dark:text-gray-400">

Select or create a note to get started

</div>

)}

  

{/* Graph View */}

<div className="h-64 border-t border-gray-200 dark:border-gray-700">

<NoteGraph

graphData={graphData}

notes={notes}

setCurrentNote={setCurrentNote}

isDarkMode={isDarkMode}

/>

  

</div>

</div>

</div>

);

};

  

export default App;
```

