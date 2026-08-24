## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs`

```diff

-5168.0.5.0.2
-  __TEXT.__text: 0x88230
-  __TEXT.__objc_methlist: 0x6724
+5168.0.55.0.0
+  __TEXT.__text: 0x880c4
+  __TEXT.__objc_methlist: 0x672c
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x3e88
-  __TEXT.__cstring: 0xb162
-  __TEXT.__oslogstring: 0x8a31
+  __TEXT.__gcc_except_tab: 0x3e2c
+  __TEXT.__cstring: 0xb1ce
+  __TEXT.__oslogstring: 0x8a0d
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x2678
+  __TEXT.__unwind_info: 0x2670
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb10
+  __DATA_CONST.__const: 0xb18
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4298
+  __DATA_CONST.__objc_selrefs: 0x42a0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x8d0
-  __AUTH_CONST.__const: 0x2dc0
-  __AUTH_CONST.__cfstring: 0x5d60
+  __AUTH_CONST.__const: 0x2da0
+  __AUTH_CONST.__cfstring: 0x5dc0
   __AUTH_CONST.__objc_const: 0xdcb8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xa20
+  __AUTH_CONST.__auth_got: 0xa30
   __AUTH.__objc_data: 0x15b8
   __AUTH.__data: 0x88
   __DATA.__objc_ivar: 0x600

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3075
-  Symbols:   6727
-  CStrings:  2147
+  Functions: 3073
+  Symbols:   6726
+  CStrings:  2150
 
Symbols:
+ +[BRSpecialFolders withSystemDataContainerForIdentifier:block:]
+ +[NSError(BRAdditions) brc_errorOrphanUploadJob]
+ -[BRContainersMonitor _checkChangesForConainerID:]
+ OBJC_IVAR_$_BRContainersMonitor._observedContainerIDsToLatestForegroundStatus
+ OBJC_IVAR_$_BRContainersMonitor._observersByContainerID
+ _BRReadOnlyShareUploadErrorCategory
+ ___50-[BRContainersMonitor _checkChangesForConainerID:]_block_invoke
+ ___block_descriptor_49_e8_32s40w_e5_v8?0l
+ _container_query_operation_set_part
+ _container_query_operation_set_part_domain
+ _objc_msgSend$_checkChangesForConainerID:
- +[BRPosixOperationsWrapper processCanUseArbitraryPersonas]
- -[BRContainersMonitor _checkChangesForContainerID:personaID:]
- BRNotifyNameForForegroundChangeWithContainerID
- OBJC_IVAR_$_BRContainersMonitor._latestContainerForegroundStatusByPersonaID
- OBJC_IVAR_$_BRContainersMonitor._observersByPersonaIDAndContainerID
- ___28-[BRContainersMonitor close]_block_invoke
- ___61-[BRContainersMonitor _checkChangesForContainerID:personaID:]_block_invoke
- ___block_descriptor_57_e8_32s40s48w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48w
- ___destroy_helper_block_e8_32s40s48w
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
