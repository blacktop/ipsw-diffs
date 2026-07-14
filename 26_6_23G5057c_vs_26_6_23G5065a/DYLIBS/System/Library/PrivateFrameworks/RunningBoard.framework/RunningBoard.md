## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
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

-  __TEXT.__text: 0x80968
+  __TEXT.__text: 0x80b28
   __TEXT.__auth_stubs: 0x1450
   __TEXT.__objc_methlist: 0x622c
   __TEXT.__const: 0x1f8
   __TEXT.__cstring: 0x7d36
-  __TEXT.__oslogstring: 0xb5f4
-  __TEXT.__gcc_except_tab: 0xca0
+  __TEXT.__oslogstring: 0xb64a
+  __TEXT.__gcc_except_tab: 0xcc8
   __TEXT.__unwind_info: 0x1e08
   __TEXT.__objc_classname: 0xf7c
-  __TEXT.__objc_methname: 0xd645
+  __TEXT.__objc_methname: 0xd665
   __TEXT.__objc_methtype: 0x2cd2
-  __TEXT.__objc_stubs: 0xa3a0
+  __TEXT.__objc_stubs: 0xa3c0
   __DATA_CONST.__got: 0x780
   __DATA_CONST.__const: 0x1798
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x178
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e68
+  __DATA_CONST.__objc_selrefs: 0x2e70
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x768
   __AUTH_CONST.__auth_got: 0xa38

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
   Functions: 2809
-  Symbols:   6115
-  CStrings:  4551
+  Symbols:   6116
+  CStrings:  4553
 
Symbols:
+ _objc_msgSend$_copyWithCorrectedInstanceUUID:
Functions:
~ -[RBLaunchdProperties _parseAdditionalProperties:] : 1528 -> 1672
~ -[RBLaunchdJobManager synchronizeJobs] : 1884 -> 2188
CStrings:
+ "_copyWithCorrectedInstanceUUID:"
+ "synchronizeJobs: correcting shared-template UUID for pid %d: %{public}@ -> %{public}@"
```
