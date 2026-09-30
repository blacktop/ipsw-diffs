## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2349.60.109.0.0
-  __TEXT.__text: 0x2b4f78
+2349.60.119.0.0
+  __TEXT.__text: 0x2b5d10
   __TEXT.__auth_stubs: 0x36b0
   __TEXT.__objc_stubs: 0x2c2c0
-  __TEXT.__objc_methlist: 0x189cc
-  __TEXT.__cstring: 0x728dd
-  __TEXT.__objc_methname: 0x3ac65
+  __TEXT.__objc_methlist: 0x189e4
+  __TEXT.__cstring: 0x72c69
+  __TEXT.__objc_methname: 0x3acde
   __TEXT.__const: 0x22c0
   __TEXT.__constg_swiftt: 0xbf4
-  __TEXT.__swift5_typeref: 0x113b
+  __TEXT.__swift5_typeref: 0x114f
   __TEXT.__swift5_reflstr: 0x1475
   __TEXT.__swift5_fieldmd: 0x149c
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x1b0
   __TEXT.__swift5_proto: 0x188
   __TEXT.__swift5_types: 0x100
-  __TEXT.__objc_classname: 0x217b
-  __TEXT.__objc_methtype: 0x6b4d
+  __TEXT.__objc_classname: 0x217d
+  __TEXT.__objc_methtype: 0x6b50
   __TEXT.__swift5_capture: 0x404
-  __TEXT.__oslogstring: 0x332f7
+  __TEXT.__oslogstring: 0x335a8
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__gcc_except_tab: 0xd00c
+  __TEXT.__gcc_except_tab: 0xd038
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x77a0
-  __TEXT.__eh_frame: 0x25c8
+  __TEXT.__unwind_info: 0x77c0
+  __TEXT.__eh_frame: 0x2630
   __DATA_CONST.__auth_got: 0x1b68
-  __DATA_CONST.__got: 0xf10
-  __DATA_CONST.__auth_ptr: 0x478
+  __DATA_CONST.__got: 0xf00
+  __DATA_CONST.__auth_ptr: 0x458
   __DATA_CONST.__const: 0x96b0
-  __DATA_CONST.__cfstring: 0x200a0
+  __DATA_CONST.__cfstring: 0x201a0
   __DATA_CONST.__objc_classlist: 0xaf0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x298

   __DATA_CONST.__objc_arraydata: 0xd48
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x4e0
-  __DATA.__objc_const: 0x2a8a0
+  __DATA.__objc_const: 0x2a8d0
   __DATA.__objc_selrefs: 0xcb00
-  __DATA.__objc_ivar: 0x1dd8
+  __DATA.__objc_ivar: 0x1ddc
   __DATA.__objc_data: 0x7958
-  __DATA.__data: 0x28b0
+  __DATA.__data: 0x28c0
   __DATA.__common: 0x49
   __DATA.__bss: 0x3570
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10806
-  Symbols:   1483
-  CStrings:  25249
+  Functions: 10813
+  Symbols:   1480
+  CStrings:  25274
 
Symbols:
- _$ss5Int32VMn
- _$ss5Int32VN
- _$ss5Int32Vs23CustomStringConvertiblesWP
CStrings:
+ "-[MBCKBackupEngine _clearPendingSnapshotAfterQuotaExceededError]"
+ "-[MBPersona(RestoreLocationAdditions) restorePathForDriveRestorable:]"
+ "=cloud-backup= Failed to stash missed encryption keys DB: %!@(MISSING)"
+ "=cloud-domain-delegate= Creating container domain for %!@(MISSING)"
+ "=cloud-domain-delegate= Creating placeholder domain for %!@(MISSING) (%!@(MISSING))"
+ "=cloud-domain-delegate= Creating skipped files domain"
+ "=cloud-domain-delegate= Creating system container domain for %!@(MISSING) at %!@(MISSING)"
+ "=cloud-domain-delegate= Creating system shared container domain for %!@(MISSING) at %!@(MISSING)"
+ "=cloud-domain-delegate= Creating uninstalled container domain for %!@(MISSING)"
+ "=drive-domain-delegate= Container domain %!@(MISSING) without an entry in manifest properties"
+ "=drive-domain-delegate= Creating system container domain for %!@(MISSING) at %!@(MISSING)"
+ "=drive-domain-delegate= Creating system shared container domain for %!@(MISSING) at %!@(MISSING)"
+ "=quota-calculation= Adding 0-byte quota usage for disabled app domain: %!@(MISSING)"
+ "=quota-calculation= Adding 0-byte quota usage for disabled static domain: %!@(MISSING)"
+ "=quota-calculation= Adding iBooksDomain size %!@(MISSING) to BooksDomain (total: %!@(MISSING))"
+ "=quota-calculation= Failed to fetch fetch app for disabled domain %!@(MISSING): %!@(MISSING)"
+ "=stashed-keys= Moved db from %!@(MISSING) -> %!@(MISSING)"
+ "=stashed-keys= No db found at %!@(MISSING)"
+ "=stashed-keys= Stashed db from %!@(MISSING) -> %!@(MISSING)"
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "Failed to scrub database - uploading original copy: %!@(MISSING)"
+ "Used after disposed"
+ "__depotRootPath"
+ "__destinationRootPath"
+ "_addZeroBytesForDisabledAndRestrictedDomainNames"
+ "_clearPendingSnapshotAfterQuotaExceededError"
+ "containerID %!@(MISSING) contains '..'"
+ "containerID %!@(MISSING) contains '/'"
+ "containerID %!@(MISSING) is `."
+ "containerID %!@(MISSING) is empty"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "initWithPlaceholderFileList:persona:cache:appManager:domainQuotasByDomainHMAC:restrictedDomains:disabledDomains:domainToSize:"
+ "restorePathForDriveRestorable:"
+ "sharedSystemContainerRestoreRootWithContainerID:"
+ "stashed-encryption-keys"
+ "stashed_encryption_keys"
+ "stashed_encryption_keys.db"
+ "systemContainerRestoreRootWithContainerID:"
+ "void _assertIfInvalidSystemContainerID(NSString *__strong)"
- "-[MBPersona(RestoreLocationAdditions) _restorePathForDomain:isSystemContainer:]"
- "-[MBPersona(RestoreLocationAdditions) restorePathForRestorable:]"
- "=quota-calculation= Adding BooksDomain size %!@(MISSING) to %!@(MISSING) (total: %!@(MISSING))"
- "@72@0:8@16@24@32@40@48@56@64"
- "Container domain %!@(MISSING) without an entry in manifest properties"
- "Creating container domain for %!@(MISSING)"
- "Creating placeholder domain for %!@(MISSING) (%!@(MISSING))"
- "Creating system container domain for %!@(MISSING)"
- "Creating system container domain for %!@(MISSING) at %!@(MISSING)"
- "Creating system shared container domain for %!@(MISSING)"
- "Creating system shared container domain for %!@(MISSING) at %!@(MISSING)"
- "Creating uninstalled container domain for %!@(MISSING)"
- "Failed closing depot FD "
- "_addSize:forDomain:"
- "_clearPendingSnapshot"
- "_depotRoot"
- "_destinationRootPath"
- "_restorePathForDomain:isSystemContainer:"
- "initWithPlaceholderFileList:persona:cache:domainQuotasByDomainHMAC:restrictedDomains:disabledDomains:domainToSize:"
- "isAppDomainName:"
- "isSystemContainerOut"
- "restorePathForRestorable:"
- "shouldRepairDomains"

```
