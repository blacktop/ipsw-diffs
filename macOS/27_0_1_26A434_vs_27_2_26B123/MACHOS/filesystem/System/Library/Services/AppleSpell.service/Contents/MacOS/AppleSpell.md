## AppleSpell

> `/System/Library/Services/AppleSpell.service/Contents/MacOS/AppleSpell`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-696.0.0.0.0
-  __TEXT.__text: 0x193614
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_stubs: 0x81c0
-  __TEXT.__objc_methlist: 0x366c
+699.0.0.0.0
+  __TEXT.__text: 0x193720
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__objc_stubs: 0x81e0
+  __TEXT.__objc_methlist: 0x3674
   __TEXT.__const: 0xb7c
-  __TEXT.__cstring: 0xc52c
+  __TEXT.__cstring: 0xc533
   __TEXT.__gcc_except_tab: 0xa7c
-  __TEXT.__objc_methname: 0xda11
-  __TEXT.__oslogstring: 0x4d8
+  __TEXT.__objc_methname: 0xda33
+  __TEXT.__oslogstring: 0x46b
   __TEXT.__objc_classname: 0x3ec
   __TEXT.__objc_methtype: 0x3d3d
   __TEXT.__ustring: 0xc62
-  __TEXT.__unwind_info: 0x25c0
+  __TEXT.__unwind_info: 0x25d0
   __DATA_CONST.__const: 0x9810
-  __DATA_CONST.__cfstring: 0xc120
+  __DATA_CONST.__cfstring: 0xc0e0
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x6a0
-  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__auth_got: 0x6c0
+  __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x4270
-  __DATA.__objc_selrefs: 0x2760
+  __DATA.__objc_selrefs: 0x2768
   __DATA.__objc_ivar: 0x45c
   __DATA.__objc_data: 0xaf0
   __DATA.__data: 0x971e
-  __DATA.__bss: 0x1390
+  __DATA.__bss: 0x1398
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2414
-  Symbols:   371
-  CStrings:  7043
+  Functions: 2417
+  Symbols:   376
+  CStrings:  7041
 
Symbols:
+ __dispatch_source_type_signal
+ _dispatch_resume
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _signal
CStrings:
+ "_addAssertionsForRequestedAssets:"
+ "com.apple.ProofReader.assetCenterBackgroundQueue"
- "At launch, %{public}llu previous assertions"
- "At launch, reset request time due to lack of previous assertions"
- "previous assertions %@"
- "reset request time"
```
