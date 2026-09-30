## ExposureNotificationDaemon

> `/System/Library/PrivateFrameworks/ExposureNotificationDaemon.framework/ExposureNotificationDaemon`

```diff

-183.9.1.1.7
-  __TEXT.__text: 0x89c8c
-  __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0x50e0
+184.40.0.0.0
+  __TEXT.__text: 0x9150c
+  __TEXT.__auth_stubs: 0x1500
+  __TEXT.__objc_methlist: 0x57bc
   __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0x1fbe5
-  __TEXT.__gcc_except_tab: 0x5040
+  __TEXT.__cstring: 0x1fc51
+  __TEXT.__gcc_except_tab: 0x50b8
   __TEXT.__oslogstring: 0x1a
-  __TEXT.__unwind_info: 0x1b28
+  __TEXT.__dlopen_cstrs: 0xb8
+  __TEXT.__unwind_info: 0x2238
   __TEXT.__objc_classname: 0x826
-  __TEXT.__objc_methname: 0x13341
+  __TEXT.__objc_methname: 0x133bd
   __TEXT.__objc_methtype: 0x25b9
   __TEXT.__objc_stubs: 0xe340
-  __DATA_CONST.__got: 0x7b8
-  __DATA_CONST.__const: 0x2380
+  __DATA_CONST.__got: 0x7b0
+  __DATA_CONST.__const: 0x23d0
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4018
+  __DATA_CONST.__objc_selrefs: 0x42b8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0xa88
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x4580
-  __AUTH_CONST.__objc_const: 0x9040
+  __AUTH_CONST.__auth_got: 0xa90
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x45c0
+  __AUTH_CONST.__objc_const: 0x8418
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xb40
-  __AUTH.__data: 0xf8
-  __DATA.__objc_ivar: 0x7a0
-  __DATA.__data: 0x16b0
+  __AUTH.__data: 0xe8
+  __DATA.__objc_ivar: 0x7a4
+  __DATA.__data: 0x1640
   __DATA.__bss: 0x51
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__data: 0x930
+  __DATA_DIRTY.__data: 0x9a0
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2168
-  Symbols:   2797
-  CStrings:  6580
+  Functions: 3085
+  Symbols:   3747
+  CStrings:  6588
 
Symbols:
+ __sl_dlopen
+ _dlerror
- _dlopen
CStrings:
+ "### LaunchApp assertion failed: bundleID %@, activity %@, PID %d"
+ "CFStringRef soft_CPPhoneNumberCopyActiveCountryCode(void)"
+ "EN is disabled for fetch"
+ "ENCoreTelephonyUtility.m"
+ "GetDiagnosisKeys %@ fromENIN:%u testing:%s refresh:%s didPrompt:%s; count:%d nextPrompt:%@ lastENIN:%u"
+ "LaunchApp assertion end: bundleID %@, activity %@, PID %d"
+ "LaunchApp completed: bundleID %@, activity %@, PID %d"
+ "NSString *soft_TPSNormalizedPhoneNumberString(NSString *__strong, NSString *__strong)"
+ "Network Proxy: %lu, EN: %s\n"
+ "No ISO country code Found for: %lu"
+ "TB,N,V_disableExposureNotification"
+ "Unsupported Exposure Notification Phase: %lu"
+ "_disableExposureNotification"
+ "disableExposureNotification"
+ "query session complete. tekCount:%u"
+ "setDisableExposureNotification:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport"
+ "softlink:r:path:/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences"
+ "submitted %d/%u for codeVerified"
+ "submitted %d/%u for keysUploaded"
+ "submitted %d/%u/%u for secondary attack"
+ "void *AppSupportLibrary(void)"
+ "void *TelephonyPreferencesLibrary(void)"
- "### LaunchApp assertion failed: bundleID %@, activity %@, PID %u"
- "/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport"
- "/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences"
- "GetDiagnosisKeys %@ fromENIN:%u testing:%s refresh:%s didPrompt:%s; count:%d nextPrompt:%@ lastENIN:%d"
- "LaunchApp assertion end: bundleID %@, activity %@, PID %u"
- "LaunchApp completed: bundleID %@, activity %@, PID %u"
- "Network Proxy: %ld, EN: %s\n"
- "No ISO country code Found for: %ld"
- "Unsupported Exposure Notification Phase: %ld"
- "f"
- "query session complete. tekCount:%d"
- "submitted %d/%d for codeVerified"
- "submitted %d/%d for keysUploaded"
- "submitted %d/%d/%d for secondary attack"

```
