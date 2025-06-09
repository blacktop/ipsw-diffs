## libNFC_HAL.dylib

> `/usr/lib/libNFC_HAL.dylib`

```diff

-355.4.0.0.0
-  __TEXT.__text: 0x17cfc
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x2af4
-  __TEXT.__oslogstring: 0x2245
-  __TEXT.__unwind_info: 0x230
+360.33.0.0.0
+  __TEXT.__text: 0x18f04
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__const: 0x120
+  __TEXT.__cstring: 0x2de5
+  __TEXT.__oslogstring: 0x2521
+  __TEXT.__unwind_info: 0x238
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x280
-  __AUTH_CONST.__auth_got: 0x3e8
-  __AUTH_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x268
+  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x380
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0x248
-  __DATA_DIRTY.__common: 0x38
+  __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  UUID: 39F9F347-E8CE-32F6-A939-A9CF190CCF52
-  Functions: 171
-  Symbols:   277
-  CStrings:  633
+  UUID: 1254D476-CA57-3C74-B31B-C41FCE0A3A8B
+  Functions: 176
+  Symbols:   275
+  CStrings:  674
 
Symbols:
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IOServiceAddInterestNotification
+ _NFHardwareGPIOSPMIvGPIO
+ _NFHardwareInterfaceRegisterSPMIErrorCallback
+ _NFHardwareInterfaceSendSPMIvGPIO
+ _NFHardwareSerialRegisterSPMIErrorCallback
+ _NFLogGetProcessNCIOnly
+ _phOsalNfc_GetMemory_Typed
+ _phTmlNfc_ParseSpmiDrvErrorStatus
+ _phTmlNfc_RegisterSpmiErrorCallback
- _NFHardwareSerialDebugDump
- _NFHardwareSerialDebugDump_wCB
- _NFHardwareSerialDebugLog
- _NFHardwareSerialDebugLogEnable
- _NFHardwareSerialDebugMaxEntriesPrinted
- _NFHardwareSerialDebugger
- _dispatch_once
- _fclose
- _fopen
- _fread
- _fseek
- _ftell
- _phOsalNfc_FreeLibrary
- _phOsalNfc_LoadLibrary
CStrings:
+ "%ld.%.3d %s %s"
+ "%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMI_CLEAR_ERRORS"
+ "%s:%i Callback already registered"
+ "%s:%i Creating IONotificationPort for %s"
+ "%s:%i Failed to issue follower reset. NACK = %d"
+ "%s:%i Failed to register SPMI error callback"
+ "%s:%i Failed to send vGPIO. NACK = %d"
+ "%s:%i Got a null buffer"
+ "%s:%i Invalid callback parameter"
+ "%s:%i Invalid phTmlNfc_e_Driver_CRC_Config"
+ "%s:%i Invalid phTmlNfc_e_Nfc_CoreDump_Trig"
+ "%s:%i Invalid phTmlNfc_e_Nfc_Tuning"
+ "%s:%i Invalid serial parameter"
+ "%s:%i NFHardwareSerialDebug size = %lu"
+ "%s:%i NFHardwareSerialDebugMsg size = %lu"
+ "%s:%i Notification subscription failed: %d"
+ "%s:%i Null serial"
+ "%s:%i Null serial internals"
+ "%s:%i Service %s not available"
+ "%s:%i Unable to create notify port"
+ "%s:%i debugger->msgListLength size = %d"
+ "%s:%i phTmlNfc_e_Nfc_CoreDump_Trig %d"
+ "%s:%i phTmlNfc_e_Nfc_Tuning %d"
+ "%s:%i s_compactTime size = %lu"
+ "%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMI_CLEAR_ERRORS"
+ "%{public}s:%i Callback already registered"
+ "%{public}s:%i Creating IONotificationPort for %s"
+ "%{public}s:%i Failed to issue follower reset. NACK = %d"
+ "%{public}s:%i Failed to register SPMI error callback"
+ "%{public}s:%i Failed to send vGPIO. NACK = %d"
+ "%{public}s:%i Got a null buffer"
+ "%{public}s:%i Invalid callback parameter"
+ "%{public}s:%i Invalid phTmlNfc_e_Driver_CRC_Config"
+ "%{public}s:%i Invalid phTmlNfc_e_Nfc_CoreDump_Trig"
+ "%{public}s:%i Invalid phTmlNfc_e_Nfc_Tuning"
+ "%{public}s:%i Invalid serial parameter"
+ "%{public}s:%i NFHardwareSerialDebug size = %lu"
+ "%{public}s:%i NFHardwareSerialDebugMsg size = %lu"
+ "%{public}s:%i Notification subscription failed: %d"
+ "%{public}s:%i Null serial"
+ "%{public}s:%i Null serial internals"
+ "%{public}s:%i Service %s not available"
+ "%{public}s:%i Unable to create notify port"
+ "%{public}s:%i debugger->msgListLength size = %d"
+ "%{public}s:%i phTmlNfc_e_Nfc_CoreDump_Trig %d"
+ "%{public}s:%i phTmlNfc_e_Nfc_Tuning %d"
+ "%{public}s:%i s_compactTime size = %lu"
+ "IOGeneralInterest"
+ "NFHardwareSerialDebugger"
+ "NFHardwareSerialRegisterSPMIErrorCallback"
+ "_NFHardwareGPIOSetValue"
+ "_NFHardwareSerialSPMIIOServiceCallback"
+ "_phTmlNfc_vGPIO"
+ "phTmlNfc_ParseSpmiDrvErrorStatus"
+ "phTmlNfc_RegisterSpmiErrorCallback"
+ "vGPIO"
- "%ld.%.6d %s %s"
- "%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMIERRORS"
- "%s:%i FAILED to allocate Memory to load FW image !!!\n"
- "%s:%i FAILED to load FW binary image file\n"
- "%s:%i error : FAILED Unable to read the specified size from file !!!\n"
- "%s:%i error : OSAL context not initialized\n"
- "%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMIERRORS"
- "%{public}s:%i FAILED to allocate Memory to load FW image !!!\n"
- "%{public}s:%i FAILED to load FW binary image file\n"
- "%{public}s:%i error : FAILED Unable to read the specified size from file !!!\n"
- "%{public}s:%i error : OSAL context not initialized\n"
- "_NFHardwareGPIOSetBoolean"
- "phOsalNfc_FreeLibrary"
- "phOsalNfc_LoadLibrary"
- "rb"

```
