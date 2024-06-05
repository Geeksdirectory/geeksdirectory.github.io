# post command 
**hugo new posts/first.md**


## add new page
add file newpage.md in content dir also add newpage.html in themes/papermod/layout/_default/newpage.html

in that file write this 
```
- identifier: tags
      name: tags
      url: /tags/
      weight: 20
```

```
---
title: ""
date: 2024-01-31T22:56:58+05:30
draft: false
categories:
  - ""
tags:
  - ""
image: ""
---

{{< printbutton print="true" >}}
```
