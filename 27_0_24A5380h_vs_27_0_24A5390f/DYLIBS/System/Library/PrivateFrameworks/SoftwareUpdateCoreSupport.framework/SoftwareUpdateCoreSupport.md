## SoftwareUpdateCoreSupport

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__oslogstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2718.0.5.0.0
-  __TEXT.__text: 0x33c90
+2718.0.12.0.0
+  __TEXT.__text: 0x33ce8
   __TEXT.__objc_methlist: 0x3544
-  __TEXT.__cstring: 0x82e7
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x674
   __TEXT.__oslogstring: 0x5248
+  __TEXT.__cstring: 0x83ba
+  __TEXT.__gcc_except_tab: 0x674
   __TEXT.__unwind_info: 0xc70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1348
+  __DATA_CONST.__const: 0x1378
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__got: 0x2a8
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x8280
+  __AUTH_CONST.__cfstring: 0x8360
   __AUTH_CONST.__objc_const: 0x4ab8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x3a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1269
-  Symbols:   3165
-  CStrings:  1304
+  Symbols:   3171
+  CStrings:  1311
 
Symbols:
+ _kSUCoreControllerPreSUStagingOptionalCountKey
+ _kSUCoreControllerPreSUStagingOptionalStagedCountKey
+ _kSUCoreControllerPreSUStagingOptionalStagedSizeKey
+ _kSUCoreControllerPreSUStagingRequiredCountKey
+ _kSUCoreControllerPreSUStagingRequiredStagedCountKey
+ _kSUCoreControllerPreSUStagingRequiredStagedSizeKey
+ _objc_msgSend$closeAndReturnError:
+ _objc_msgSend$synchronizeAndReturnError:
- _objc_msgSend$closeFile
- _objc_msgSend$synchronizeFile
CStrings:
+ "failed to fsync persistence file"
+ "preSUStagingOptionalCount"
+ "preSUStagingOptionalStagedCount"
+ "preSUStagingOptionalStagedSize"
+ "preSUStagingRequiredCount"
+ "preSUStagingRequiredStagedCount"
+ "preSUStagingRequiredStagedSize"
```
