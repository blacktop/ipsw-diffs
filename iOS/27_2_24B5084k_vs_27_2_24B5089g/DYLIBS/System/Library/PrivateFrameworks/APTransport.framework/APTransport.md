## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-1005.7.1.0.0
-  __TEXT.__text: 0xb3740
+1005.8.1.0.0
+  __TEXT.__text: 0xb4350
   __TEXT.__objc_methlist: 0x1d2c
   __TEXT.__const: 0x674
   __TEXT.__gcc_except_tab: 0xa10
-  __TEXT.__cstring: 0x3095b
+  __TEXT.__cstring: 0x30ebc
   __TEXT.__dlopen_cstrs: 0x1f3
   __TEXT.__oslogstring: 0x31c
-  __TEXT.__unwind_info: 0x4560
+  __TEXT.__unwind_info: 0x4578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x400
   __AUTH_CONST.__const: 0x2d78
-  __AUTH_CONST.__cfstring: 0x6640
+  __AUTH_CONST.__cfstring: 0x6660
   __AUTH_CONST.__objc_const: 0x24f8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x78

   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x2c0
   __DATA.__objc_ivar: 0x18c
-  __DATA.__data: 0x14a0
+  __DATA.__data: 0x1430
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__data: 0xc40
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA_DIRTY.__data: 0xcb0
+  __DATA_DIRTY.__bss: 0x2c8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5345
-  Symbols:   5034
-  CStrings:  4565
+  Functions: 5361
+  Symbols:   5044
+  CStrings:  4587
 
Symbols:
+ GCC_except_table36
+ GCC_except_table45
+ GCC_except_table63
+ GCC_except_table69
+ GCC_except_table70
+ _APAdvertiserInfoCopyNameWithoutMDNSLabelSuffix
+ _APBrowserSetAirPlayInfo
+ _APTransportDeviceForwardAirPlayInfoToBrowser
+ _FigCFSetContainsValue
+ _FigCFSetGetCount
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ ___APBrowserSetAirPlayInfo_block_invoke
+ ___strlcpy_chk
- GCC_except_table26
- GCC_except_table31
- GCC_except_table34
- GCC_except_table61
- GCC_except_table62
- GCC_except_table67
- GCC_except_table68
- __APAdvertiserInfoCopyAndRemoveMDNSLabelSuffix
CStrings:
+ "%s external AirPlay info for device with id: %@ name: %'@ from source: [%{ptr}]"
+ "1005.8.1"
+ "APAdvertiserInfoCopyNameWithoutMDNSLabelSuffix"
+ "APBrowserSetAirPlayInfo"
+ "APTransportDeviceForwardAirPlayInfoToBrowser"
+ "Add external source [%{ptr}] for device with id: %@. %ld registered sources"
+ "Dropping external AirPlay info for device with id: %@. Last source withdrew"
+ "Dropping external AirPlay info for device with id: %@: deviceInfo caught up"
+ "External AirPlay info for device with id: %@ is held until Discovery finds it"
+ "ExternalInfoSources"
+ "Failed to create advertiser info for %@."
+ "OSStatus browser_addOrUpdateExternalAirPlayInfo(APBrowserRef, CFNumberRef, CFNumberRef, CFStringRef, CFDataRef)"
+ "OSStatus browser_createAdvertiserInfoForDevice(APBrowserRef, CFNumberRef, CFDictionaryRef, APAdvertiserInfoRef *)"
+ "OSStatus browser_removeExternalAirPlayInfo(APBrowserRef, CFNumberRef, CFNumberRef)"
+ "Remove external source [%{ptr}] for device with id: %@. %ld registered sources"
+ "Update"
+ "[%{ptr}] Deleted old capture file (%s; freed %lu bytes, %lu bytes / %lu file(s) remain): %s\n"
+ "[%{ptr}] Enforcing storage limits: %lu evictable capture file(s), %lu bytes across all captures (limits: %d file(s), %d bytes)\n"
+ "[%{ptr}] Most recent capture (%lu bytes) alone exceeds the %d-byte budget; keeping it instead of deleting the just-completed snoop\n"
+ "browser_addOrUpdateExternalAirPlayInfo"
+ "browser_copyEffectiveAirPlayInfo"
+ "browser_removeExternalAirPlayInfo"
+ "browser_setAirPlayInfo"
+ "over file-count limit"
+ "over size budget"
+ "void browser_dropExternalAirPlayInfoIfDeviceInfoCaughtUp(APBrowserRef, CFNumberRef, CFDictionaryRef)"
- "1005.7.1"
- "OSStatus browser_createAdvertiserInfoForDevice(CFAllocatorRef, CFDictionaryRef, LogCategory *, APAdvertiserInfoRef *)"
- "[%{ptr}] Deleted old capture file: %s\n"
- "_APAdvertiserInfoCopyAndRemoveMDNSLabelSuffix"
```
