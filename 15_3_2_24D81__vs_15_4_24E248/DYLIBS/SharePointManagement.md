## SharePointManagement

> `/System/Library/PrivateFrameworks/SharePointManagement.framework/Versions/A/SharePointManagement`

```diff

-294.9.0.0.0
-  __TEXT.__text: 0x4888
+302.3.0.0.0
+  __TEXT.__text: 0x4828
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x414
+  __TEXT.__objc_methlist: 0x584
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x3b8
   __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__oslogstring: 0x29c
-  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__unwind_info: 0x1b0
   __TEXT.__objc_classname: 0xb1
   __TEXT.__objc_methname: 0xf29
   __TEXT.__objc_methtype: 0x3d1

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d0
+  __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0x1f0
   __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0xc48
+  __AUTH_CONST.__objc_const: 0x9b0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x238

   - /System/Library/Frameworks/OpenDirectory.framework/Versions/A/OpenDirectory
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AA4F2ED-60B4-33D2-BBA2-803D308E3A58
-  Functions: 131
-  Symbols:   443
+  UUID: 6C925FFA-56EB-3171-84A3-177458B1FEDE
+  Functions: 138
+  Symbols:   460
   CStrings:  340
 
Symbols:
+ +[SPMSharePoint isURLShareable:].cold.1
+ +[SPMSharePoint(OpenDirectory) attributesToFetch].cold.1
+ +[SPMSharePointManager sharedInstance].cold.1
+ -[NSURL(SPMAdditions) __spm_fileSecurity].cold.1
+ -[NSURL(SPMAdditions) __spm_isHFSStandard].cold.2
+ -[NSURL(SPMAdditions) __spm_isLocalVolume].cold.2
+ -[NSURL(SPMAdditions) __spm_isWriteable].cold.1
+ -[NSURL(SPMAdditions) __spm_localizedName].cold.2
+ -[NSURL(SPMAdditions) __spm_supportsPermissions].cold.1
+ -[NSURL(SPMAdditions) __spm_volumeURL].cold.2
+ -[SPMSharePoint(OpenDirectory) initWithRecord:].cold.2
+ -[SPMSharePointManager _addSharePointNamed:withInfo:].cold.1
+ -[SPMSharePointManager _records].cold.1
+ -[SPMSharePointManager _records].cold.2
+ -[SPMSharePointManager addSharePoint:error:].cold.2
+ -[SPMSharePointManager removeSharePoint:error:].cold.2
+ -[SPMSharePointManager updateSharePoint:error:].cold.2

```
