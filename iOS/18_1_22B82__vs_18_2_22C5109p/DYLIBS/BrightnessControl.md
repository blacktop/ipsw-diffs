## BrightnessControl

> `/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`

```diff

-1835.40.30.0.0
-  __TEXT.__text: 0x89a8
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0x404
-  __TEXT.__const: 0x3f88
-  __TEXT.__gcc_except_tab: 0x1e4
-  __TEXT.__cstring: 0xb1b
-  __TEXT.__oslogstring: 0x935
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__objc_classname: 0x70
-  __TEXT.__objc_methname: 0xb7a
-  __TEXT.__objc_methtype: 0x20d
-  __TEXT.__objc_stubs: 0xe00
-  __DATA_CONST.__got: 0xe0
+1850.60.91.0.0
+  __TEXT.__text: 0x9cac
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0x4a8
+  __TEXT.__const: 0x3fa8
+  __TEXT.__gcc_except_tab: 0x1f4
+  __TEXT.__cstring: 0xbd0
+  __TEXT.__oslogstring: 0xb76
+  __TEXT.__unwind_info: 0x318
+  __TEXT.__objc_classname: 0x8d
+  __TEXT.__objc_methname: 0xd78
+  __TEXT.__objc_methtype: 0x297
+  __TEXT.__objc_stubs: 0xf60
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x388
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x398
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x410
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x268
+  __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0x9b8
+  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__objc_const: 0xb88
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xac
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0x4
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x28
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/AFKUser.framework/AFKUser
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 211
-  Symbols:   345
-  CStrings:  416
+  Functions: 235
+  Symbols:   389
+  CStrings:  468
 
Symbols:
+ _IOCFSerialize
+ _IOCFUnserializeBinary
+ _IOObjectRetain
+ _IOServiceMatching
+ _OBJC_CLASS_$_AFKEndpointInterface
+ _OBJC_CLASS_$_APToDCPEndpoint
+ _OBJC_CLASS_$_CBAPEndpoint
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_METACLASS_$_APToDCPEndpoint
+ _OBJC_METACLASS_$_CBAPEndpoint
+ ___strlcpy_chk
+ __os_signpost_emit_with_name_impl
+ _kIOMainPortDefault
+ _mach_continuous_time
+ _memcpy
+ _objc_release_x22
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_signpost_enabled
+ _strlcpy
CStrings:
+ "%!s(MISSING):%!s(MISSING) called for key: %!s(MISSING)"
+ "%!s(MISSING):%!s(MISSING) called for key: %!s(MISSING), property: %!@(MISSING)"
+ "-[CBAPEndpoint copyProperty:]"
+ "-[CBAPEndpoint setProperty:property:]"
+ "0x%!x(MISSING)"
+ "0x%!x(MISSING), status: %!d(MISSING)"
+ "@\"AFKEndpointInterface\""
+ "@\"CBAPEndpoint\""
+ "@24@0:8@16"
+ "@32@0:8@16@24"
+ "AFKEndpointInterface"
+ "APToDCPEndpoint"
+ "B32@0:8@16@24"
+ "B36@0:8i16r^v20Q28"
+ "B48@0:8i16r^v20Q28^@36I44"
+ "CBAFKEndpointQueue"
+ "CBAPEndpoint"
+ "CBAPToDCPService"
+ "Could not encode value for setting property %!s(MISSING), value: %!@(MISSING)\n"
+ "Data for setting property %!s(MISSING) is too long, max payload %!l(MISSING)u, needed size %!l(MISSING)u\n"
+ "ERROR initializing CBAPEndpoint for service: %!s(MISSING)"
+ "ERROR! enqueueCommandSync failed result:0x%!x(MISSING)"
+ "ERROR: %!s(MISSING) sevice not found"
+ "ERROR: unable to serialize outputBuffer: %!@(MISSING)"
+ "I32@0:8@16@24"
+ "IONameMatch"
+ "Property name is too long, %!s(MISSING)\n"
+ "Response received from DCP: %!@(MISSING)"
+ "Send OOB command = 0x%!x(MISSING)"
+ "Send command = 0x%!x(MISSING)"
+ "WARNING: Property name is too long it will be truncated, %!s(MISSING) -> %!s(MISSING)\n"
+ "_endpoint"
+ "_epQueue"
+ "_service"
+ "activate:"
+ "addEntriesFromDictionary:"
+ "com.apple.CoreBrightness.CBAPEndpoint"
+ "copyProperty:"
+ "enqueueCommandSync"
+ "enqueueCommandSync:inputBuffer:inputBufferSize:responseObj:options:"
+ "enqueueCommandSync:timestamp:inputBuffer:inputBufferSize:responseTimestamp:outputBuffer:inOutBufferSize:options:"
+ "findDCPServiceWithName:role:"
+ "initWithLength:"
+ "initWithServiceName:role:"
+ "isEqualToString:"
+ "lengthOfBytesUsingEncoding:"
+ "mutableBytes"
+ "role"
+ "sendCommand:inputBuffer:inputBufferSize:"
+ "sendOOBCommand:inputBuffer:inputBufferSize:"
+ "setProperty:property:"
+ "sharedInstance"

```
