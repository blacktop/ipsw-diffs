## AppleMobileBackup

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/MobileDevice.framework/Versions/A/AppleMobileDeviceHelper.app/Contents/Resources/AppleMobileBackup`

```diff

-2349.80.25.0.0
-  __TEXT.__text: 0xe844
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0x1a40
-  __TEXT.__objc_methlist: 0x804
-  __TEXT.__const: 0x4a0
-  __TEXT.__cstring: 0x4aeb
+2624.100.106.0.0
+  __TEXT.__text: 0xc5cc
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_stubs: 0x1880
+  __TEXT.__objc_methlist: 0x81c
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x3f56
   __TEXT.__objc_classname: 0xc8
   __TEXT.__objc_methtype: 0x39a
-  __TEXT.__objc_methname: 0x16cf
-  __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x3a0
-  __TEXT.__eh_frame: 0x128
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x298
-  __DATA_CONST.__cfstring: 0x24c0
+  __TEXT.__objc_methname: 0x15b8
+  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__eh_frame: 0xb4
+  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__cfstring: 0x1e00
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x8c0
-  __DATA.__objc_selrefs: 0x7d0
-  __DATA.__objc_classrefs: 0x108
+  __DATA.__objc_const: 0x8a0
+  __DATA.__objc_selrefs: 0x760
+  __DATA.__objc_classrefs: 0x100
   __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x370
-  __DATA.__data: 0x3d8
-  __DATA.__bss: 0x160
-  __DATA.__common: 0x8
+  __DATA.__data: 0x3d4
+  __DATA.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/DeviceLink.framework/Versions/A/DeviceLink
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3EA59E8B-C652-3CB8-9D24-4FFA3F3F0718
-  Functions: 320
-  Symbols:   202
-  CStrings:  1231
+  UUID: 0F770939-6481-3B55-A8B3-038075E1D388
+  Functions: 248
+  Symbols:   167
+  CStrings:  1066
 
Symbols:
- _CFBundleGetVersionNumber
- _CFDataGetBytes
- _CFPreferencesCopyValue
- _CFPreferencesSynchronize
- _CFUUIDCreate
- _CFUUIDCreateString
- _NSInvalidArgumentException
- _OBJC_CLASS_$_NSLocale
- __Unwind_Resume
- ___objc_personality_v0
- _dispatch_queue_attr_make_with_autorelease_frequency
- _dispatch_queue_create
- _dispatch_sync
- _kCFPreferencesAnyApplication
- _kCFPreferencesAnyHost
- _kCFPreferencesCurrentUser
- _kill
- _mkdtemp
- _pipe
- _posix_spawn
- _posix_spawn_file_actions_addinherit_np
- _posix_spawn_file_actions_destroy
- _posix_spawn_file_actions_init
- _posix_spawnattr_destroy
- _posix_spawnattr_init
- _posix_spawnattr_setflags
- _pthread_mutex_init
- _pthread_mutex_lock
- _pthread_mutex_unlock
- _puts
- _random
- _snprintf
- _stat
- _strdup
- _waitpid
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileBackup/Common/Source/MBComputerManager.m"
- "%0.1f GB"
- "%0.1f KB"
- "%0.1f MB"
- "%ld B"
- "%s %s Null data\n"
- "%s %s:\n%s\n"
- "%s/XXXXXXXXXXXXXXX"
- "%s: Can't create child\n"
- "%s: Can't create child...\n"
- "%s: Can't read message, child isn't running\n"
- "%s: Can't talk to child\n"
- "%s: NULL response dict read, try sending command again...\n"
- "%s: write to child failed, trying to create child again...\n"
- "*** Error initializing mutex for ProcessLink Lock: %d!!! The application may step all over itself without this lock to protext it!\n"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MobileBackup/Common/Source/MBComputerManager.m"
- "/var/mobile"
- "/var/mobile/Library/SafeHarbor"
- "/var/tmp/backupd-XXXXXXXXXXXXXXX"
- "000000000000"
- "13A343"
- "9.0"
- "AMSProcessLinkReadMessageFromChild called without valid ProcessLink object\n"
- "AMSProcessLinkSendMessage called without valid ProcessLink object\n"
- "AMSProcessLinkSendMessageAsync called without valid ProcessLink object\n"
- "AMSProcessLinkSendMessageLock called without valid ProcessLink object\n"
- "AppleLanguages"
- "BOOL MBSnapshotFormatContainsAssets(MBSnapshotFormat)"
- "BOOL MBSnapshotFormatContainsFileLists(MBSnapshotFormat)"
- "BOOL MBSnapshotFormatContainsManifests(MBSnapshotFormat)"
- "BOOL MBSnapshotFormatSupportedForBackup(MBSnapshotFormat)"
- "BOOL _isSourceIdentifierRequired(MBAction)"
- "Can't allocate args with size %d (%d bytes)\n"
- "Can't create child read pipe, error %d: %s\n"
- "Can't create child write pipe, error %d: %s\n"
- "Child with pid %d exited normally\n"
- "DeviceUDID=\"%{public}@\", DeviceUUID=\"%@\", DeviceName=\"%@\", ProductType=\"%{public}@\", ProductVersion=%{public}@, BuildVersion=%{public}@"
- "DomainsAssets"
- "EEE, dd MMM yyyy HH:mm:ss z"
- "Exec of child with pid %d failed with error %d\n"
- "MBTempPathUtils.m"
- "MBTemporaryPath"
- "Manifest.db"
- "Manifest.mbdb"
- "Manifest.mbdx"
- "ManifestsFiles"
- "ManifestsFilesAndDomains"
- "ManifestsFilesAndDomainsAssets"
- "N61"
- "NSString *MBStringForBackupReason(MBBackupReason)"
- "NSString *MBStringForSnapshotFormat(MBSnapshotFormat)"
- "NSString *MBTemporaryPath(void)"
- "NSString *MBTemporaryPath(void)_block_invoke"
- "Null path"
- "Parent"
- "Platform2 == PLATFORM_MACOS && \"unexpected platform\""
- "Preference %@ %@ not a dictionary"
- "ProcessLinkLog"
- "Removing temporary directory at %{public}@"
- "SQL"
- "Simulator"
- "Snapshot"
- "The child path is empty, so we can't create a child process"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (strdup)"
- "Unable to obtain MBTemporaryPath()"
- "Unexpected action"
- "Unknown backup reason %lu"
- "Unknown snapshot format %llu"
- "Unknown snapshot format reason %llu"
- "Unspecified"
- "Warning! Can't lock ProcessLink Lock to send message to child: %d\n"
- "Warning! Can't unlock ProcessLink Lock after sending message to child: %d\n"
- "__isPlatformOrVariantPlatformVersionAtLeast"
- "_sendMessage called without valid ProcessLink object\n"
- "automatic"
- "automaticOnBattery"
- "automaticOnCellular"
- "black"
- "characterAtIndex:"
- "com.apple.DeviceLink"
- "compare:options:"
- "currentLocale"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "download"
- "en_US"
- "full"
- "full-seed"
- "iPhone 5"
- "iPhone5,1"
- "incremental"
- "inherited"
- "initWithLocaleIdentifier:"
- "initWithUTF8String:"
- "initial"
- "manual"
- "mktemp failed: %{errno}d"
- "mobile"
- "os_version_check.c"
- "posix_spawn failed, error %d: %s\n"
- "raise:format:"
- "setDateFormat:"
- "setFormatterBehavior:"
- "setLocale:"
- "setWithObjects:"
- "stringByStandardizingPath"
- "subarrayWithRange:"
- "substringFromIndex:"
- "unspecified"
- "upload"
- "yyyy-MM-dd HH:mm:ss.SSS"
- "~/"

```
