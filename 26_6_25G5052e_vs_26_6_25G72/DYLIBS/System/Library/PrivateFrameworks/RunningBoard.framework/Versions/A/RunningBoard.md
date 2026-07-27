## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/Versions/A/RunningBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1015.100.16.0.0
-  __TEXT.__text: 0x864b4
+1015.160.2.0.1
+  __TEXT.__text: 0x86690
   __TEXT.__auth_stubs: 0x1350
   __TEXT.__objc_methlist: 0x61b4
-  __TEXT.__const: 0x248
+  __TEXT.__const: 0x240
   __TEXT.__cstring: 0x6cc2
-  __TEXT.__oslogstring: 0xb157
-  __TEXT.__gcc_except_tab: 0xc58
+  __TEXT.__oslogstring: 0xb1ad
+  __TEXT.__gcc_except_tab: 0xc80
   __TEXT.__unwind_info: 0x1c20
   __TEXT.__objc_classname: 0xf4a
-  __TEXT.__objc_methname: 0xd181
+  __TEXT.__objc_methname: 0xd1a1
   __TEXT.__objc_methtype: 0x2d6a
-  __TEXT.__objc_stubs: 0x9ec0
+  __TEXT.__objc_stubs: 0x9ee0
   __DATA_CONST.__got: 0x758
   __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ce0
+  __DATA_CONST.__objc_selrefs: 0x2ce8
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x738
   __AUTH_CONST.__auth_got: 0x9b8

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
   Functions: 2880
-  Symbols:   6136
-  CStrings:  4372
+  Symbols:   6137
+  CStrings:  4374
 
Symbols:
+ _objc_msgSend$_copyWithCorrectedInstanceUUID:
Functions:
~ -[RBLaunchdJobManager synchronizeJobs] : 1940 -> 2256
~ -[RBLaunchdProperties _parseAdditionalProperties:] : 1588 -> 1748
CStrings:
+ "_copyWithCorrectedInstanceUUID:"
+ "synchronizeJobs: correcting shared-template UUID for pid %d: %{public}@ -> %{public}@"
```
