## GenerationalStorage

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/GenerationalStorage`

```diff

-384.60.3.0.0
-  __TEXT.__text: 0x1b744
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0xaec
+384.100.2.0.0
+  __TEXT.__text: 0x1b80c
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_methlist: 0xe04
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x156a
+  __TEXT.__cstring: 0x1564
   __TEXT.__oslogstring: 0x7b2
   __TEXT.__gcc_except_tab: 0x51c
-  __TEXT.__unwind_info: 0x658
+  __TEXT.__unwind_info: 0x670
   __TEXT.__objc_classname: 0x1ab
   __TEXT.__objc_methname: 0x250b
   __TEXT.__objc_methtype: 0x100e

   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x4c8
+  __AUTH_CONST.__auth_got: 0x4c0
   __AUTH_CONST.__const: 0x790
   __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x1ec0
+  __AUTH_CONST.__objc_const: 0x18f8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_ivar: 0xec

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC1EC70B-AD31-3544-A0BC-F1E12089AE7B
-  Functions: 479
-  Symbols:   1416
-  CStrings:  957
+  UUID: DA28835A-07BD-3255-9353-C1F9DBF20959
+  Functions: 489
+  Symbols:   1423
+  CStrings:  955
 
Symbols:
+ +[GSDaemonProxySync proxy].cold.1
+ -[GSClientManagedLibrary initWithURL:error:].cold.1
+ -[GSPermanentStorage _invalidate].cold.1
+ -[GSStagingPrefix _invalidate:].cold.1
+ -[GSStorageManager readImportCookieDataForVolumeAtURL:handler:].cold.1
+ -[GSSystemManagedLibrary initWithURL:clientID:error:].cold.1
+ -[GSTemporaryStorage initWithLibraryURL:forItemAtURL:error:].cold.1
+ GSDaemonConnectionClose.cold.1
+ GSDaemonInterface.cold.1
+ GSDaemonProxy.cold.1
+ GSLibraryResolveDocumentId2.cold.1
+ GSLibraryResolveDocumentIdCachedAPFS.cold.3
+ gs_default_log.cold.1
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _strncmp
CStrings:
- ".."
- "._"

```
