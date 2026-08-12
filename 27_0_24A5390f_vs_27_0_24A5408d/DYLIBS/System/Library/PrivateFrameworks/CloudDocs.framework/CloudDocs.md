## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-5168.0.5.0.2
-  __TEXT.__text: 0x7f248
-  __TEXT.__objc_methlist: 0x66dc
+5168.0.55.0.0
+  __TEXT.__text: 0x7f1a8
+  __TEXT.__objc_methlist: 0x66e4
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x3bc0
-  __TEXT.__cstring: 0xb830
-  __TEXT.__oslogstring: 0x8d46
+  __TEXT.__gcc_except_tab: 0x3b68
+  __TEXT.__cstring: 0xb89c
+  __TEXT.__oslogstring: 0x8d22
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2650
+  __TEXT.__unwind_info: 0x2648
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x24a0
+  __DATA_CONST.__const: 0x24a8
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4240
+  __DATA_CONST.__objc_selrefs: 0x4248
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__got: 0x8d8
-  __AUTH_CONST.__const: 0x1080
-  __AUTH_CONST.__cfstring: 0x5f00
+  __AUTH_CONST.__const: 0x1060
+  __AUTH_CONST.__cfstring: 0x5f60
   __AUTH_CONST.__objc_const: 0xdb30
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xa50
+  __AUTH_CONST.__auth_got: 0xa60
   __AUTH.__objc_data: 0x16d0
   __AUTH.__data: 0xc8
   __DATA.__objc_ivar: 0x5e8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 3032
-  Symbols:   6518
-  CStrings:  2199
+  Symbols:   6519
+  CStrings:  2202
 
Symbols:
+ +[BRSpecialFolders withSystemDataContainerForIdentifier:block:]
+ +[NSError(BRAdditions) brc_errorOrphanUploadJob]
+ -[BRContainersMonitor _checkChangesForConainerID:]
+ OBJC_IVAR_$_BRContainersMonitor._observersByContainerID
+ OBJC_IVAR_$_BRContainersMonitor._queue
+ _BRReadOnlyShareUploadErrorCategory
+ _OBJC_IVAR_$_BRContainersMonitor._observedContainerIDsToLatestForegroundStatus
+ ___50-[BRContainersMonitor _checkChangesForConainerID:]_block_invoke
+ ___block_descriptor_49_e8_32s40w_e5_v8?0lw40l8s32l8
+ _container_query_operation_set_part
+ _container_query_operation_set_part_domain
+ _objc_msgSend$_checkChangesForConainerID:
- +[BRPosixOperationsWrapper processCanUseArbitraryPersonas]
- -[BRContainersMonitor _checkChangesForContainerID:personaID:]
- GCC_except_table24
- _OBJC_IVAR_$_BRContainersMonitor._latestContainerForegroundStatusByPersonaID
- _OBJC_IVAR_$_BRContainersMonitor._observersByPersonaIDAndContainerID
- _OBJC_IVAR_$_BRContainersMonitor._queue
- ___28-[BRContainersMonitor close]_block_invoke
- ___61-[BRContainersMonitor _checkChangesForContainerID:personaID:]_block_invoke
- ___block_descriptor_57_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- _objc_msgSend$_checkChangesForContainerID:personaID:
- _objc_msgSend$processCanUseArbitraryPersonas
CStrings:
+ "+[BRSpecialFolders withSystemDataContainerForIdentifier:block:]"
+ "-[BRContainersMonitor _checkChangesForConainerID:]"
+ "-[BRContainersMonitor _checkChangesForConainerID:]_block_invoke"
+ "5168.0.55"
+ "Failed to lookup systemData container for %@: %s"
+ "Got NULL path for systemData container %@ (%s)"
+ "[DEBUG] %@ is now %s%@"
+ "[DEBUG] Container %@ foreground changed (%@ -> %d)%@"
+ "[DEBUG] Failed to consume systemData sandbox token for %@: (%s)%@"
+ "[DEBUG] Notifying that container %@ is now %s%@"
+ "[DEBUG] ┏%llx Adding observer for %@%@"
+ "[DEBUG] ┏%llx Removing observer for %@%@"
+ "readOnlyShareUpload"
- "-[BRContainersMonitor _checkChangesForContainerID:personaID:]"
- "-[BRContainersMonitor _checkChangesForContainerID:personaID:]_block_invoke"
- "5168.0.5.0.2"
- "BRNotifyNameForForegroundChangeWithContainerID"
- "[CRIT] Assertion failed: personaID%@"
- "[DEBUG] %@ (persona %@) is now %s%@"
- "[DEBUG] Container %@ (persona %@) foreground changed (%@ -> %d)%@"
- "[DEBUG] Notifying that container %@ (persona %@) is now %s%@"
- "[DEBUG] ┏%llx Adding observer for %@ (persona %@)%@"
- "[DEBUG] ┏%llx Removing observer for %@ (persona %@)%@"
```
