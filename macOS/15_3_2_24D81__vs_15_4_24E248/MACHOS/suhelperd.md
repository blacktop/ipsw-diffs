## suhelperd

> `/System/Library/CoreServices/Software Update.app/Contents/Resources/suhelperd`

```diff

-2078.80.2.0.2
-  __TEXT.__text: 0xd1a8
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0x1ca0
-  __TEXT.__objc_methlist: 0x4f0
-  __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__oslogstring: 0x1401
-  __TEXT.__cstring: 0x14b4
-  __TEXT.__objc_methname: 0x19ee
-  __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methtype: 0x476
+2078.101.1.0.0
+  __TEXT.__text: 0xd0e0
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_stubs: 0x1c80
+  __TEXT.__objc_methlist: 0x6a4
+  __TEXT.__const: 0xa0
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__oslogstring: 0x1481
+  __TEXT.__cstring: 0x14aa
+  __TEXT.__objc_methname: 0x1a42
+  __TEXT.__objc_classname: 0xa9
+  __TEXT.__objc_methtype: 0x481
   __TEXT.__dof_SoftwareU: 0x1f2
-  __TEXT.__unwind_info: 0x320
-  __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x938
+  __TEXT.__unwind_info: 0x328
+  __DATA_CONST.__auth_got: 0x458
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x8b8
   __DATA_CONST.__cfstring: 0x1460
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x118
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0xbe8
+  __DATA.__objc_const: 0x808
   __DATA.__objc_selrefs: 0x7b8
   __DATA.__objc_ivar: 0x4c
-  __DATA.__objc_data: 0x280
-  __DATA.__data: 0x90
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x68
   __DATA.__common: 0x8
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2307DBF4-AE10-3BF5-96D5-9B38F813EEB7
-  Functions: 270
-  Symbols:   234
-  CStrings:  809
+  UUID: 9D76DA61-5BAF-3436-B491-7F269E3D7115
+  Functions: 264
+  Symbols:   236
+  CStrings:  810
 
Symbols:
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _IOPMAssertionCreateWithProperties
+ _OBJC_CLASS_$_SUUtilities
+ _SUHelperDMachServiceName
+ _SULoginWindowCookiePath
+ __SULogObject
+ _kCFAllocatorDefault
+ _kCFBooleanTrue
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _su_firmware_updates_directory
+ _su_shared_updates_directory
- _CFPreferencesGetAppBooleanValue
- _CFPreferencesSynchronize
- _NSOpenStepRootDirectory
- _OBJC_CLASS_$_NSProcessInfo
- _SUPrefDomain
- _kCFPreferencesAnyUser
- _kCFPreferencesCurrentHost
- _os_log_copy_message_string
- _os_log_create
- _os_log_set_hook
- _strcmp
CStrings:
+ " - Display Sleep Assertion"
+ "%@: Asking CacheDelete to free %lld bytes (can free %lld bytes)"
+ "%s: CacheDelete can free %lld bytes."
+ "%s: Device already has enough space"
+ "%s: Display sleep prevention failed."
+ "%s: Preventing display sleep with assertion %@."
+ "-[SUHelper attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:]"
+ "-[SUHelper cacheDeletePurgeableSpace]"
+ "-[SUPowerAssertionManager createUserActivityAssertionWithDescription:timeout:]"
+ "AppliesOnLidClose"
+ "AssertName"
+ "AssertType"
+ "Q16@0:8"
+ "TimeoutSeconds"
+ "UserIsActive"
+ "cacheDeletePurgeableSpace"
+ "createCacheDeleteInfoDictionaryWithUrgencyLevel:spaceToPurge:"
+ "createUserActivityAssertionWithDescription:timeout:"
+ "numberWithDouble:"
+ "prepareForLogoutAndInstall"
+ "v32@0:8@16d24"
- "%@: %@ logging to install.log."
- "%@: Asked CacheDelete to free %lld bytes (can free %lld bytes)"
- "/Library/Updates"
- "/Library/Updates/Firmware"
- "/var/db/.SoftwareUpdateAtLogout"
- "/var/run/SoftwareUpdatesAvailable"
- "CACHE_DELETE_URGENCY"
- "CACHE_DELETE_VOLUME"
- "SUDebugVeryVerbose"
- "SUSharedPaths"
- "com.apple.suhelperd"
- "enabling"
- "i20@0:8B16"
- "not enabling"
- "numberWithLongLong:"
- "prepareForLogoutAndInstall:"
- "processInfo"
- "processName"
- "removeUpdatesAvailableCookie"
- "v20@?0C8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}12"

```
