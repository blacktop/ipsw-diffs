## demod_helper

> `/usr/libexec/demod_helper`

```diff

-1246.2.4.0.0
-  __TEXT.__text: 0x2ba10
-  __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__objc_stubs: 0x3e80
-  __TEXT.__objc_methlist: 0x18e4
-  __TEXT.__cstring: 0x4e29
-  __TEXT.__objc_methname: 0x44fb
+1254.42.1.0.0
+  __TEXT.__text: 0x2cb90
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_stubs: 0x3f40
+  __TEXT.__objc_methlist: 0x192c
+  __TEXT.__cstring: 0x4f08
+  __TEXT.__objc_methname: 0x4615
   __TEXT.__objc_classname: 0x1c9
   __TEXT.__objc_methtype: 0x593
+  __TEXT.__oslogstring: 0x56a0
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__oslogstring: 0x5494
+  __TEXT.__gcc_except_tab: 0x250
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x73c
-  __DATA_CONST.__auth_got: 0x7f0
-  __DATA_CONST.__got: 0x1c8
+  __TEXT.__unwind_info: 0x760
+  __DATA_CONST.__auth_got: 0x7f8
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x40e0
+  __DATA_CONST.__cfstring: 0x4240
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_arraydata: 0x210
   __DATA_CONST.__objc_arrayobj: 0x210
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x17d0
-  __DATA.__objc_selrefs: 0x1388
+  __DATA.__objc_const: 0x1800
+  __DATA.__objc_selrefs: 0x13c0
   __DATA.__objc_classrefs: 0x1b0
   __DATA.__objc_superrefs: 0x60
-  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x85c
   __DATA.__bss: 0x160

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1918137E-AA8E-37F6-B3D0-DFF8668FA778
-  Functions: 1021
-  Symbols:   355
-  CStrings:  2460
+  UUID: 44F0B1CF-B509-3330-9BB7-71A426614FC3
+  Functions: 1034
+  Symbols:   357
+  CStrings:  2498
 
Symbols:
+ ___kCFBooleanTrue
+ _objc_retain_x28
CStrings:
+ "\x18"
+ "%s: entered - Launching test script is not supported on this OS!"
+ "-[MSDDemoManifestCheck runSecurityCheck:]"
+ "-[MSDDemoManifestCheck runSecurityCheck:]_block_invoke"
+ "-[MSDDemoManifestCheck secureManifestCheckForSegmentedManifest:options:]"
+ "-[MSDDemoManifestCheck verifyManifestSignature:forDataSectionKeys:withOptions:]"
+ "Cannot find RelativePathsNotToBackupInMegaBackup under HomeKitDomain."
+ "Cannot find RelativePathsNotToBackupToService under HomeKitDomain."
+ "Cannot find RelativePathsToOnlyBackupEncrypted under HomeKitDomain."
+ "Cannot find RelativePathsToRemoveOnRestore under HomeKitDomain."
+ "Cannot find RelativePathsToRestoreOnly under HomeKitDomain."
+ "Excluding %{public}@ from section: %{public}@ component:%{public}@"
+ "ExlcudeBlocklistItem"
+ "Hex strings should have an even number of digits (%@)"
+ "HomeKitDomain"
+ "Library/homed/datastore.sqlite"
+ "Library/homed/datastore.sqlite-shm"
+ "Library/homed/datastore.sqlite-wal"
+ "Library/homed/protected-home.config"
+ "MinimumOSVersion"
+ "No items blocklisted, skip blocklist item exclusion"
+ "ProductVersion"
+ "RelativePathsNotToBackupInMegaBackup"
+ "RigorousTestingOverride"
+ "String should be all hex digits: %@ (bad digit around %ld)"
+ "T@\"NSMutableSet\",&,V_blocklistedItems"
+ "Unable to malloc bytes of size: %lu"
+ "_blocklistedItems"
+ "blocklistedItems"
+ "copy"
+ "realitydevice"
+ "removeBlocklistedItemFromSection:withName:"
+ "runFileSecurityChecksForSection:dataType:options:"
+ "runSecurityCheck:"
+ "runSecurityChecksForSection:dataType:componentName:options:"
+ "secureManifestCheckForSegmentedManifest:options:"
+ "setBlocklistedItems:"
+ "verifyFactoryManifestSignature:forDataSectionKeys:"
+ "verifyManifestSignature:forDataSectionKeys:withOptions:"
- "\x17"
- "%s: %{public}@ key does not exist"
- "%s: %{public}@ key in wrong format"
- "%s: entered - Launching test script is not supported on customer OS!"
- "-[MSDDemoManifestCheck runSecurityCheck]"
- "-[MSDDemoManifestCheck runSecurityCheck]_block_invoke"
- "-[MSDDemoManifestCheck secureManifestCheckForSegmentedManifest:]"
- "-[MSDDemoManifestCheck verifyManifestSignature:forDataSectionKeys:withRigorousTestingOverride:]"
- "-[NSDictionary(xpcdictConv) objectForKey:ofType:]"
- "runSecurityCheck"
- "runSecurityChecksForSection:dataType:componentName:"
- "verifyManifestSignature:forDataSectionKeys:withRigorousTestingOverride:"

```
