## BulletinBoard

> `/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-952.0.0.0.0
-  __TEXT.__text: 0x748c0
-  __TEXT.__objc_methlist: 0x860c
-  __TEXT.__const: 0x170
+953.100.0.0.0
+  __TEXT.__text: 0x786f4
+  __TEXT.__objc_methlist: 0x862c
+  __TEXT.__const: 0x190
   __TEXT.__gcc_except_tab: 0x9b8
-  __TEXT.__cstring: 0x62a4
-  __TEXT.__oslogstring: 0x5eea
+  __TEXT.__cstring: 0x6426
+  __TEXT.__oslogstring: 0x65ef
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__unwind_info: 0x20a0
+  __TEXT.__unwind_info: 0x20b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f90
+  __DATA_CONST.__const: 0x2038
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3fb8
+  __DATA_CONST.__objc_selrefs: 0x3fc0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x170
   __DATA_CONST.__got: 0x5b8
   __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x6960
-  __AUTH_CONST.__objc_const: 0x107a8
+  __AUTH_CONST.__cfstring: 0x6be0
+  __AUTH_CONST.__objc_const: 0x107b8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x8c4
   __DATA.__data: 0xe00
   __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0x1720
+  __DATA_DIRTY.__objc_data: 0x18b0
   __DATA_DIRTY.__data: 0x14
   __DATA_DIRTY.__bss: 0x1a8
   __DATA_DIRTY.__common: 0x70

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3355
-  Symbols:   6836
-  CStrings:  1378
+  Functions: 3365
+  Symbols:   6847
+  CStrings:  1431
 
Symbols:
+ -[BBBiometricResource isPasscodeSet]
+ -[BBSectionInfo changedPropertiesComparedTo:]
+ -[BBSectionInfoSettings changedPropertiesComparedTo:]
+ _BBStringFromBBAlertType
+ _BBStringFromBBAuthorizationStatus
+ _BBStringFromBBBulletinGroupingSetting
+ _BBStringFromBBSectionAnnounceSetting
+ _BBStringFromBBSectionCategory
+ _BBStringFromBBSectionInfoSetting
+ _BBStringFromBBSectionType
+ _objc_msgSend$changedPropertiesComparedTo:
CStrings:
+ "%s: %@"
+ "%s: %@ -> %@"
+ "%{public}@: Read %lu BBSectionInfo entries from persistence"
+ "%{public}@: Read section info (version=%{public}@, encoded count=%lu)"
+ "%{public}@: Reading BBSectionInfo from persistence at %{public}@"
+ "%{public}@: Reading cleared sections from persistence"
+ "%{public}@: initialized"
+ "%{public}@: setSectionInfoByID count=%lu"
+ "(new) "
+ "BBPersistentStoreMigrator: decoded %lu section infos for migration"
+ "BBPersistentStoreMigrator: no migration needed (on-disk version already %lu)"
+ "BBPersistentStoreMigrator: on-disk version=%lu, target=%lu, encoded section count=%lu"
+ "BBPersistentStoreMigrator: running section ID migration"
+ "BBPersistentStoreMigrator: starting section info migration (target version %lu)"
+ "BBPersistentStoreMigrator: upgrading to version 1 (remove vestigial sections + content preview migration)"
+ "BBPersistentStoreMigrator: upgrading to version 2 (sanitize push settings)"
+ "BBPersistentStoreMigrator: v3 migration complete (locked=%lu, healed=%lu)"
+ "BBPersistentStoreMigrator: will migrate (needsSectionIDMigration=%{BOOL}d, versionBump=%{BOOL}d)"
+ "BBPersistentStoreMigrator: writing migrated section info (count=%lu) at version %lu"
+ "BBServer startup: loaded %lu section infos from persistent store"
+ "BBServer startup: loading data providers"
+ "BBServer startup: loading data providers and settings"
+ "BBServer startup: resuming XPC listeners"
+ "Effective content preview setting: %{public}@, raw: %{public}@, globalSetting: %{public}@, isLocked: %@"
+ "Protection state changed for %{public}@: wasLocked:%d isLocked=%d contentPreviewSetting=%ld"
+ "Writing section info with reason: '%{public}@'"
+ "[%{public}@] \tNew = %{public}@"
+ "[%{public}@] \tOld = %{public}@"
+ "[%{public}@] %{public}@: changed: {%{public}@}"
+ "[%{public}@] %{public}@: read from disk: %{public}@"
+ "[%{public}@] %{public}@: setSectionInfo changed: {%{public}@}"
+ "[%{public}@] Got effective contentPreviewSetting for lockedApp: %{public}@"
+ "[%{public}@] Saving updated section info changed: {%{public}@}"
+ "[%{public}@] loaded: %{public}@"
+ "[%{public}@] v3 migration: resetting content preview setting from ShowNever to Default for locked app"
+ "[%{public}@] v3 migration: setIsLocked=YES, contentPreviewSetting=%ld"
+ "announcePriorityNotificationsSetting"
+ "authorized"
+ "bulletins"
+ "denied"
+ "directMessagesSetting"
+ "enabledAll"
+ "enabledTimeSensitive"
+ "hasUserConfiguredDirectMessagesSetting"
+ "hasUserConfiguredTimeSensitiveSetting"
+ "invalid"
+ "managedSectionInfoSettings: {%@}"
+ "modal"
+ "none"
+ "notDetermined"
+ "notSupported"
+ "off"
+ "parentSection"
+ "provisional"
+ "sectionInfoSettings: {%@}"
+ "subsection"
+ "temporary"
+ "weeApp"
- "Protection state changed for %{public}@: isLocked=%d contentPreviewSetting=%ld"
- "Reading BBSectionInfo from persistence"
- "Reading cleared sections from persistence"
- "Resetting content preview setting from ShowNever to Default for locked app \"%{public}@\""
- "Saving updated section info for: %{public}@\n\tOld = %{public}@\n\tNew = %{public}@"
```
