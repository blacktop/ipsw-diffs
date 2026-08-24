## com.apple.Notes.SpotlightIndexExtension

> `/System/Applications/Notes.app/Contents/PlugIns/com.apple.Notes.SpotlightIndexExtension.appex/Contents/MacOS/com.apple.Notes.SpotlightIndexExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-3192.0.0.0.0
-  __TEXT.__text: 0x2d54
+3195.0.0.0.0
+  __TEXT.__text: 0x2e34
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_stubs: 0x600
   __TEXT.__objc_methlist: 0x104
   __TEXT.__gcc_except_tab: 0x208
   __TEXT.__const: 0x42
   __TEXT.__cstring: 0x23b
-  __TEXT.__oslogstring: 0x3e7
-  __TEXT.__objc_methname: 0x750
+  __TEXT.__oslogstring: 0x454
+  __TEXT.__objc_methname: 0x756
   __TEXT.__objc_classname: 0x16
   __TEXT.__objc_methtype: 0xbd
   __TEXT.__unwind_info: 0x160

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 67
+  Functions: 68
   Symbols:   90
-  CStrings:  124
+  CStrings:  125
 
Functions:
~ sub_100002fa4 : 320 -> 500
+ sub_100004120
CStrings:
+ "Index extension wants to reindex specific items but in-extension indexing is disabled. Deferring to the app."
+ "reindexSearchableItemsWithObjectIDURIs:scope:completionHandler:"
- "reindexSearchableItemsWithObjectIDURIs:completionHandler:"
```
