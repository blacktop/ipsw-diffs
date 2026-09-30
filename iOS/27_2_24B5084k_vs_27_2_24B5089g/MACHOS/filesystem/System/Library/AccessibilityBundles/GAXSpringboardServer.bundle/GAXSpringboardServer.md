## GAXSpringboardServer

> `/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1067.3.0.0.0
-  __TEXT.__text: 0x15af4
+1067.3.1.0.0
+  __TEXT.__text: 0x15ba0
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x2f60
   __TEXT.__objc_methlist: 0x1edc

   __TEXT.__gcc_except_tab: 0x464
   __TEXT.__cstring: 0x50c2
   __TEXT.__objc_methname: 0x599e
-  __TEXT.__oslogstring: 0x1ad7
+  __TEXT.__oslogstring: 0x1bc8
   __TEXT.__objc_classname: 0xcff
   __TEXT.__objc_methtype: 0x1000
   __TEXT.__unwind_info: 0x820

   - /usr/lib/libobjc.A.dylib
   Functions: 552
   Symbols:   557
-  CStrings:  1596
+  CStrings:  1599
 
Functions:
~ sub_431c : 300 -> 412
~ sub_44b4 -> sub_4524 : 184 -> 244
CStrings:
+ "Guided Access is trying to make the system aperture inert, but we already have an assertion."
+ "Ignoring request for system aperture to become inert, Guided Access is not running."
+ "No system aperture inert assertion held, nothing to invalidate."
```
