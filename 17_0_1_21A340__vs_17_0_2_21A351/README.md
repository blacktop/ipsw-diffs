# 17.0.1 (21A340) .vs 17.0.2 (21A351)

## IPSWs

- `iPhone15,2_17.0.1_21A340_Restore.ipsw`
- `iPhone15,2_17.0.2_21A351_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.0.1 *(21A340)* | 23.0.0 | 10002.2.12~1 | Fri, 15Sep2023 13:43:33 PDT |
| 17.0.2 *(21A351)* | 23.0.0 | 10002.2.12~1 | Fri, 15Sep2023 13:43:33 PDT |

## MachO

### ⬆️ Updated (15)

<details>
  <summary><i>View Updated</i></summary>

#### MBHelperApp

>  `/Applications/MBHelperApp.app/MBHelperApp`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x86c
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_stubs: 0x3c0

   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32C42AC7-86F4-36E9-A897-B4DF84FFB0F6
+  UUID: 2B351707-DA5D-38D5-905C-9C3189F0C4BA
   Functions: 27
   Symbols:   47
   CStrings:  261

```

#### MBPrebuddyAccountNotificationPlugin

>  `/System/Library/Accounts/Notification/MBPrebuddyAccountNotificationPlugin.bundle/MBPrebuddyAccountNotificationPlugin`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x638
   __TEXT.__auth_stubs: 0x120
   __TEXT.__objc_stubs: 0x140

   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 48B72AAD-784B-3BFB-A016-EAFE9E992B7C
+  UUID: 73B6D657-26A2-338F-BCF3-21D530190C38
   Functions: 5
   Symbols:   44
   CStrings:  87

```

#### RestorePostProcess

>  `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x12a2c
   __TEXT.__auth_stubs: 0xc70
   __TEXT.__objc_stubs: 0x1fa0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5469644D-5D1F-3316-8084-9141C39AE08E
+  UUID: 574C18D0-983E-3FAF-9A64-30BFBE8AC117
   Functions: 291
   Symbols:   266
   CStrings:  1142

```

#### MobileBackupCacheDeleteService

>  `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x5750
   __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_stubs: 0xee0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3764A750-9171-371F-A4D4-105B3524B0A9
+  UUID: 989E7D33-352F-344A-A504-BD7F151B7D5E
   Functions: 100
   Symbols:   111
   CStrings:  417

```

#### MBDiagnosticExtension

>  `/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBDiagnosticExtension.appex/MBDiagnosticExtension`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x27c
   __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_stubs: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 364693EB-99D9-358C-8884-A9FCB3510823
+  UUID: EF462774-F223-3AE4-A978-CE0B395B01D6
   Functions: 3
   Symbols:   36
   CStrings:  32

```

#### MBFollowUpExtension

>  `/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBFollowUpExtension.appex/MBFollowUpExtension`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x10a0
   __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x3c0

   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F345FA4-93B0-3C6F-A7C1-BE95659CFCA8
+  UUID: 999279A1-954A-37B1-AF4F-0214ED1AA659
   Functions: 14
   Symbols:   57
   CStrings:  104

```

#### MBPrebuddyFollowUpExtension

>  `/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBPrebuddyFollowUpExtension.appex/MBPrebuddyFollowUpExtension`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0xd630
   __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_stubs: 0x2c60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 29E1E223-2764-3A9F-9599-E9D18E3300B1
+  UUID: D8FFEB78-874F-342B-9CFD-7AD98EA9848F
   Functions: 281
   Symbols:   221
   CStrings:  1058

```

#### MBHelperService

>  `/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x109f8
   __TEXT.__auth_stubs: 0xa80
   __TEXT.__objc_stubs: 0x1e00

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F2736248-9C5D-3B3F-84A5-745EB49F78A9
+  UUID: BC9CE769-3378-328B-94E5-8D4D9750C238
   Functions: 312
   Symbols:   266
   CStrings:  1135

```

#### backupd

>  `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x2177c4
   __TEXT.__auth_stubs: 0x2d30
   __TEXT.__objc_stubs: 0x25b60

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 703D1A99-4B39-31F2-87D4-A778CFD439C6
+  UUID: 6B774173-CFEE-3B29-BA6B-61FD2635816E
   Functions: 8308
   Symbols:   1241
   CStrings:  25289

```

#### MBATCPlugin

>  `/System/Library/SyncBundles/MBATCPlugin.syncBundle/MBATCPlugin`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0xad8
   __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_stubs: 0x260

   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C013392-F78A-3555-BD54-D5ADF2A873AC
+  UUID: 4F9439D4-4593-3429-8A5F-47F60ADF38E6
   Functions: 11
   Symbols:   51
   CStrings:  168

```

#### MobileBackupUEA

>  `/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x498c
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_stubs: 0xba0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9FD708F1-A5A2-3579-87ED-85001F0C350B
+  UUID: 66C5CBF3-0E48-3CAC-A9B9-EC7EF712B16E
   Functions: 86
   Symbols:   132
   CStrings:  435

```

#### dyld

>  `/usr/lib/dyld`

```diff

-1122.2.0.0.0
+1123.2.0.0.0
   __TEXT.__text: 0x77644
   __TEXT.__const: 0x1690
   __TEXT.__cstring: 0xc9c1

   __DATA_DIRTY.__data: 0x5c
   __DATA_DIRTY.__common: 0x1120
   __DATA_DIRTY.__bss: 0x1bc0
-  UUID: C8BDB7D4-5C57-3429-B5BF-707B7CC0F494
+  UUID: 8841081F-A678-367E-B229-E7DA02370901
   Functions: 2838
   Symbols:   3257
   CStrings:  1634
CStrings:
+ "1123.2"
- "1122.2"

```

#### BackupAgent2

>  `/usr/libexec/BackupAgent2`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x7ff2c
   __TEXT.__auth_stubs: 0x1770
   __TEXT.__objc_stubs: 0xc500

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F904F3E8-41CE-393F-9B1E-73FAB887653F
+  UUID: 84C33F0C-96F9-35D4-8D56-85B4807F633C
   Functions: 2120
   Symbols:   549
   CStrings:  8302

```

#### FinishRestoreFromBackup

>  `/usr/libexec/FinishRestoreFromBackup`

```diff

-1996.2.2.0.0
-  __TEXT.__text: 0x2e0c
+1996.2.3.0.0
+  __TEXT.__text: 0x2e40
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x1684
+  __TEXT.__cstring: 0x169c
   __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__auth_got: 0x260
   __DATA_CONST.__got: 0x48

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 897A44D4-1526-357F-B290-5B2A36844CC8
+  UUID: 416838E0-A11D-3AAA-BCA2-FD73D3161F73
   Functions: 41
   Symbols:   90
-  CStrings:  262
+  CStrings:  263
 
CStrings:
+ "nameSize cannot be zero"

```

#### SyncAgent

>  `/usr/libexec/SyncAgent`

```diff

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4788E560-3497-3BCD-83AC-3D68D09BF674
+  UUID: D149BA7A-D045-37A4-94CA-1A4D5B884BEB
   Functions: 41
   Symbols:   136
   CStrings:  408

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.0.1 *(21A340)* | 616.1.27.10.15 |
| 17.0.2 *(21A351)* | 616.1.27.10.15 |

### Dylibs

#### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### MobileSyncAccountNotificationPlugin

>  `/System/Library/Accounts/Notification/MobileSyncAccountNotificationPlugin.bundle/MobileSyncAccountNotificationPlugin`

```diff

   - /System/Library/PrivateFrameworks/MobileSync.framework/MobileSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C02461C8-C249-32B3-AF04-0F2F83522A48
+  UUID: 51B99B99-34BA-33F7-B7D5-7D3AF3C95E7A
   Functions: 5
   Symbols:   53
   CStrings:  75

```

#### MobileBackup

>  `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-1996.2.2.0.0
+1996.2.3.0.0
   __TEXT.__text: 0x43538
   __TEXT.__auth_stubs: 0xf30
   __TEXT.__objc_methlist: 0x4844

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9DAA0335-E092-37CC-857A-2B8E8BF8BD40
+  UUID: E97A1FF6-41C0-3551-8DFC-491000992CDE
   Functions: 1877
   Symbols:   5915
   CStrings:  4856

```

#### MobileSync

>  `/System/Library/PrivateFrameworks/MobileSync.framework/MobileSync`

```diff

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A2BCE7D5-607D-3207-A65A-57EB89C8C4A3
+  UUID: 5E4BFD86-B9AA-3162-9E42-14075BA7217C
   Functions: 188
   Symbols:   984
   CStrings:  1605

```

#### dyld

>  `/usr/lib/dyld`

```diff

-1122.2.0.0.0
+1123.2.0.0.0
   __TEXT.__text: 0x77644
   __TEXT.__const: 0x1690
   __TEXT.__cstring: 0xc9c1

   __DATA_DIRTY.__data: 0x5c
   __DATA_DIRTY.__common: 0x1120
   __DATA_DIRTY.__bss: 0x1bc0
-  UUID: C8BDB7D4-5C57-3429-B5BF-707B7CC0F494
+  UUID: 8841081F-A678-367E-B229-E7DA02370901
   Functions: 2838
   Symbols:   6074
   CStrings:  1634
CStrings:
+ "1123.2"
- "1122.2"

```

#### libdyld.dylib

>  `/usr/lib/system/libdyld.dylib`

```diff

-1122.2.0.0.0
+1123.2.0.0.0
   __TEXT.__text: 0x20ef8
   __TEXT.__auth_stubs: 0x610
   __TEXT.__const: 0x580

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 46F17C9D-029C-3CFE-AEC4-E71B407619B4
+  UUID: DE6100E4-59F8-30A0-A85D-AAC196665780
   Functions: 948
   Symbols:   1943
   CStrings:  174

```


</details>

## Files

### 🆕 New

#### SystemOS (2)

- `/.fseventsd/000000000676f908`
- `/.fseventsd/000000000676f909`

## EOF
