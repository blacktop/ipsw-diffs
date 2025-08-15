## MessagesDataMigrator

> `/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator`

```diff

-1261.200.71.2.16
-  __TEXT.__text: 0x1234
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0x50
+1262.300.81.2.13
+  __TEXT.__text: 0xd28
+  __TEXT.__auth_stubs: 0x1a0
+  __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0x412
-  __TEXT.__oslogstring: 0x3dd
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__cstring: 0x80
+  __TEXT.__oslogstring: 0x2e2
+  __TEXT.__unwind_info: 0xbc
   __TEXT.__objc_classname: 0x15
-  __TEXT.__objc_methname: 0x193
-  __TEXT.__objc_methtype: 0x2e
-  __TEXT.__objc_stubs: 0x160
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__objc_methname: 0x1fa
+  __TEXT.__objc_methtype: 0x39
+  __TEXT.__objc_stubs: 0x1e0
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x48
-  __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__objc_selrefs: 0x90
+  __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x100
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_classrefs: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B3A15C87-4628-3DE3-90F4-5E27B1C8B150
-  Functions: 8
-  Symbols:   65
-  CStrings:  59
+  UUID: FBA09064-7424-352D-B6F6-C64BAA478BAE
+  Functions: 11
+  Symbols:   67
+  CStrings:  41
 
Symbols:
+ _IMCloudKitAnalyticSyncDatesDictionaryKey
+ _IMCloudKitDefinesAttemptEnableMiCOnUnlock
+ _IMCloudKitDefinesClearSyncStore
+ _IMCloudKitDefinesDidUpgradeOrRestoreFromBackup
+ _IMCloudKitDefinesVerifyFirstRestoreDateVersion
+ _IMCloudKitMiCDeviceIdentifierKey
- _MarcoLogMadridLevel
- _MarcoShouldLogMadridLevel
- __IMAlwaysLog
- __IMWillLog
CStrings:
+ "%@:\n\t\t{domain: %@ key %@ originalValue: %{BOOL}d}\n\t\t{domain: %@ key %@ originalValue: %{BOOL}d}\n\t\t{domain: %@ key %@ originalValue: %{BOOL}d}\n\t\t{domain: %@ key %@ originalValue: %{BOOL}d}\n\t\t{domain: %@ key %@ originalValue: %{BOOL}d}\n\t\t{domain: %@ key %@ originalValue: %{BOOL}d}"
+ "Finished clearing with new values"
+ "We are restoring a device from backup ---- clearing defaults"
+ "_cloudKitEnabled"
+ "_didRestoreFromDeviceToDevice"
+ "_printCriticalDefaultsWithMessage:"
+ "clearMOCDefaultsForRestoreFromBackupIfNeeded {didRestoreFromBackUp: %{BOOL}d, didRestoreFromCloudBackUp: %{BOOL}d, didRestoreFromDeviceToDevice: %{BOOL}d, didUpgrade: %{BOOL}d, disposition: %d}"
+ "userDataDisposition"
+ "v24@0:8@16"
- "After clearing -- cloudkitEnabled %@ hasPerformedNewDeviceBringup %@ hasPerformedIniatialSyncOnImagentLaunch %@ hasTriedAutoEnrollingMOC %@"
- "Finished clearing with new values:\n \t\t{domain: %@ key %@ originalValue: %@}\n \t\t{domain: %@ key %@ originalValue: %@}\n \t\t{domain: %@ key %@ originalValue: %@}\n \t\t{domain: %@ key %@ originalValue: %@}\n \t\t{domain: %@ key %@ originalValue: %@}"
- "IMFoundation"
- "NO"
- "We are restoring a device from backup ---- clearing defaults:\n \t\t{domain: %@ key %@ originalValue: %@}\n \t\t{domain: %@ key %@ originalValue: %@}\n \t\t{domain: %@ key %@ originalValue: %@}\n \t\t{domain: %@ key %@ originalValue: %@}"
- "YES"
- "clearMOCDefaultsForRestoreFromBackupIfNeeded {didRestoreFromBackUp: %@, didRestoreFromCloudBackUp: %@, didUpgrade: %@}"

```
