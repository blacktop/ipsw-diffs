## DACoreDAVGlue

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue`

```diff

-2691.2.2.0.0
-  __TEXT.__text: 0xc1c
-  __TEXT.__auth_stubs: 0x220
+2691.4.5.0.0
+  __TEXT.__text: 0xc6c
+  __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x20
   __TEXT.__oslogstring: 0x17b
   __TEXT.__gcc_except_tab: 0x20
   __TEXT.__cstring: 0xd
-  __TEXT.__unwind_info: 0xa8
+  __TEXT.__unwind_info: 0xa0
   __TEXT.__objc_classname: 0x75
   __TEXT.__objc_methname: 0x5de
   __TEXT.__objc_methtype: 0x1e3

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0x108
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0xa78

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B31EF5EE-6D5C-3E3D-B563-FFB4CC93EEDB
+  UUID: 91CC3FBE-7698-3A50-A69B-808F6EE83306
   Functions: 24
-  Symbols:   189
+  Symbols:   186
   CStrings:  132
 
Symbols:
+ _objc_release_x26
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ _coreDAVValidationErrorFromRawError : 604 -> 628
~ -[CoreDAVTask(DACoreDAVGlueExtensions) cancelTaskWithReason:underlyingError:] : 344 -> 356
~ -[DACoreDAVTaskManager _updateSpinner:] : 964 -> 980
~ -[DACoreDAVTaskManager dealloc] : 500 -> 508
~ +[DACoreDAVLogger registerDefaultLoggerWithCoreDAV] : 68 -> 84
~ ___51+[DACoreDAVLogger registerDefaultLoggerWithCoreDAV]_block_invoke : 124 -> 128

```
