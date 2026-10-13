## AppleMCTF

> `System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-913.63.1.0.0
-  __TEXT.__text: 0x88ff0
+913.64.1.0.0
+  __TEXT.__text: 0x8905c
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x28d9b
+  __TEXT.__cstring: 0x28dcb
   __TEXT.__const: 0x22a98
   __TEXT.__gcc_except_tab: 0x62c
   __TEXT.__objc_methname: 0xb

   - /usr/lib/libobjc.A.dylib
   Functions: 678
   Symbols:   346
-  CStrings:  3473
+  CStrings:  3474
 
Functions:
~ sub_eb8 : 4856 -> 4884
~ sub_21b0 -> sub_21cc : 4588 -> 4616
~ sub_339c -> sub_33d4 : 7120 -> 7148
~ sub_35658 -> sub_356ac : 1008 -> 1004
~ sub_48010 -> sub_48060 : 11216 -> 11224
~ sub_4c4d0 -> sub_4c528 : 7768 -> 7784
~ sub_7cdd0 -> sub_7ce38 : 40 -> 44
CStrings:
+ "913.64.1"
+ "MachThreadPriorityForThreadEmittingFrames = %d\n"
- "913.63.1"
```
