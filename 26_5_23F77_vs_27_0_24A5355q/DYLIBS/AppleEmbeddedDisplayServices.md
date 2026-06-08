## AppleEmbeddedDisplayServices

> `/System/Library/PrivateFrameworks/AppleEmbeddedDisplayServices.framework/AppleEmbeddedDisplayServices`

```diff

-201.100.3.0.0
-  __TEXT.__text: 0x1514
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x109
-  __TEXT.__oslogstring: 0x2a1
-  __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x123
-  __TEXT.__objc_stubs: 0x180
-  __DATA_CONST.__got: 0x48
+226.0.0.502.1
+  __TEXT.__text: 0x18f8
+  __TEXT.__const: 0x18
+  __TEXT.__cstring: 0x122
+  __TEXT.__oslogstring: 0x2fc
+  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xe0
+  __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/AFKUser.framework/AFKUser
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1CB31859-AEEA-3029-BF81-D3F7271C153D
-  Functions: 33
-  Symbols:   132
-  CStrings:  45
+  UUID: AD2137B5-C311-3935-A7DD-48898F895F01
+  Functions: 37
+  Symbols:   142
+  CStrings:  38
 
Symbols:
+ _BIMUpdaterCreateWithIndex
+ _BIMUpdaterReadRaw
+ _BIMUpdaterWriteRaw
+ _CFDataGetBytes
+ _CFDataGetLength
+ _CFDataGetTypeID
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryGetParentEntry
+ ___eepromServiceCB.cold.2
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_retain
+ _objc_retain_x8
- _objc_release_x22
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x22
CStrings:
+ "Display index %u exceeds maximum supported value %u"
+ "Failed to set EEPROM instance ID: 0x%x"
+ "IOService"
+ "display-index"
- "acquireAndWaitForPowerOn"
- "activate:"
- "cancel"
- "createPowerAssertionWithReason:identifier:"
- "enqueueCommandSync:timestamp:inputBuffer:inputBufferSize:responseTimestamp:outputBuffer:inOutBufferSize:options:"
- "invalidate"
- "isEqual:"
- "mainDisplay"
- "setDispatchQueue:"
- "setEventHandler:"
- "stateControl"
- "withService:"

```
