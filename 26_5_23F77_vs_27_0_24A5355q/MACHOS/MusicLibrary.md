## MusicLibrary

> `/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary`

```diff

-4025.600.4.0.0
-  __TEXT.__text: 0x7abec
-  __TEXT.__auth_stubs: 0x850
+4026.110.62.2.0
+  __TEXT.__text: 0x1c725c
+  __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_stubs: 0x4ca0
-  __TEXT.__objc_methlist: 0x11b4
+  __TEXT.__objc_methlist: 0x11d4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__const: 0xf814
-  __TEXT.__gcc_except_tab: 0xe34
-  __TEXT.__objc_methname: 0x5f0b
-  __TEXT.__objc_classname: 0x224
+  __TEXT.__const: 0x1e1f4
+  __TEXT.__gcc_except_tab: 0xdbc
+  __TEXT.__objc_methname: 0x5f71
+  __TEXT.__objc_classname: 0x20a
+  __TEXT.__cstring: 0x2848
   __TEXT.__objc_methtype: 0xbec
-  __TEXT.__cstring: 0x280b
-  __TEXT.__oslogstring: 0x46f2
-  __TEXT.__unwind_info: 0x880
-  __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__auth_got: 0x438
-  __DATA_CONST.__got: 0x610
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x5c40
+  __TEXT.__oslogstring: 0x472a
+  __TEXT.__unwind_info: 0x988
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__const: 0x124c0
   __DATA_CONST.__cfstring: 0x1a00
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_arraydata: 0x258
   __DATA_CONST.__objc_arrayobj: 0x300
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1388
-  __DATA.__objc_selrefs: 0x1870
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x618
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA.__objc_const: 0x1390
+  __DATA.__objc_selrefs: 0x1880
   __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0xa10
+  __DATA.__data: 0x1208
   __DATA.__bss: 0x200
-  __DATA.__common: 0xa1c
+  __DATA.__common: 0xb20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation

   - /System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic
   - /System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/HomeSharing.framework/HomeSharing
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 01361C73-FEFC-31F2-BAD5-42755EF89F4E
-  Functions: 567
-  Symbols:   355
-  CStrings:  1784
+  UUID: 6F9CBC54-A781-36E8-AEAD-04EB7127AA5F
+  Functions: 751
+  Symbols:   387
+  CStrings:  1789
 
Symbols:
+ _IOConnectCallStructMethod
+ _IOIteratorNext
+ _IOMainPort
+ _IOObjectRelease
+ _IOServiceGetMatchingServices
+ _IOServiceMatching
+ _IOServiceOpen
+ _ML3MusicLibraryCloudLibraryAvailablityDidChangeNotification
+ __xpc_type_dictionary
+ __xpc_type_int64
+ _abort
+ _dlclose
+ _dlopen
+ _getpid
+ _mmap
+ _munmap
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
+ _proc_pidpath
+ _sched_yield
+ _strnlen
+ _sysconf
+ _sysctlbyname
+ _xpc_connection_activate
+ _xpc_connection_create_mach_service
+ _xpc_connection_send_message_with_reply_sync
+ _xpc_connection_set_event_handler
+ _xpc_copy_description
+ _xpc_dictionary_create
+ _xpc_dictionary_get_data
+ _xpc_dictionary_get_value
+ _xpc_dictionary_set_data
+ _xpc_get_type
+ _xpc_int64_get_value
+ _xpc_release
- _bootstrap_look_up
- _bootstrap_port
- _malloc_type_malloc
- _objc_autorelease
- _objc_release_x2
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "Enqueueing asset upload request: %{public}@"
+ "NanoMusicSync"
+ "NewAutomaticDownloads"
+ "Updated keep_local:%d, keep_local_status:%d for track:%lld with status:%d"
+ "Updated keep_local:%d, keep_local_status:%d for track:%lld with status:%d error=%{public}@"
+ "_libraryCloudLibraryAvailabilityDidChange:"
+ "assetLinkController:willCancelActiveDownloadsOfMediaTypes:"
+ "cloud library availability changed - requesting a sync"
- "Enqueuing asset upload request: %{public}@"
- "Updated keep_local:%d, keep_lcoal_status:%d for track:%lld with status:%d"
- "Updated keep_local:%d, keep_lcoal_status:%d for track:%lld with status:%d error=%{public}@"

```
