## SoftwareUpdateCoreSupport

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__oslogstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__objc_ivar`
- `__DATA.__data`

```diff

-2718.0.5.0.0
-  __TEXT.__text: 0x387ec
+2718.0.12.501.1
+  __TEXT.__text: 0x3884c
   __TEXT.__objc_methlist: 0x3554
-  __TEXT.__cstring: 0x84e2
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x6c0
   __TEXT.__oslogstring: 0x531a
+  __TEXT.__cstring: 0x85b5
+  __TEXT.__gcc_except_tab: 0x6c0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xbf0
+  __TEXT.__unwind_info: 0xbe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__const: 0xb50
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__got: 0x2c8
   __AUTH_CONST.__const: 0xa70
-  __AUTH_CONST.__cfstring: 0x8540
+  __AUTH_CONST.__cfstring: 0x8620
   __AUTH_CONST.__objc_const: 0x4ab8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x2c0
-  __AUTH.__objc_data: 0x618
+  __AUTH.__objc_data: 0x438
   __DATA.__objc_ivar: 0x460
   __DATA.__data: 0x180
   __DATA.__bss: 0xb0
-  __DATA_DIRTY.__objc_data: 0x2f8
+  __DATA_DIRTY.__objc_data: 0x4d8
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
   Functions: 1314
-  Symbols:   3198
-  CStrings:  1337
+  Symbols:   3204
+  CStrings:  1344
 
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
