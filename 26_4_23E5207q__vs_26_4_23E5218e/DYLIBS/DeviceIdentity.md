## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`

```diff

-1076.100.26.0.0
-  __TEXT.__text: 0x1c794
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x4b4
-  __TEXT.__cstring: 0x3dfc
+1076.100.28.0.0
+  __TEXT.__text: 0x1cd24
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_methlist: 0x504
+  __TEXT.__cstring: 0x3e98
   __TEXT.__const: 0xabaa
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x6e3
   __TEXT.__gcc_except_tab: 0xa14
   __TEXT.__dlopen_cstrs: 0x134
-  __TEXT.__unwind_info: 0x3c8
+  __TEXT.__unwind_info: 0x3d8
   __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x16a3
-  __TEXT.__objc_methtype: 0x320
-  __TEXT.__objc_stubs: 0xfc0
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x36b8
+  __TEXT.__objc_methname: 0x1778
+  __TEXT.__objc_methtype: 0x349
+  __TEXT.__objc_stubs: 0x10a0
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0x36c0
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x648
+  __DATA_CONST.__objc_selrefs: 0x690
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x4e8
-  __AUTH_CONST.__auth_got: 0x428
+  __DATA_CONST.__objc_arraydata: 0x4f0
+  __AUTH_CONST.__auth_got: 0x440
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x42c0
-  __AUTH_CONST.__objc_const: 0x740
+  __AUTH_CONST.__cfstring: 0x43e0
+  __AUTH_CONST.__objc_const: 0x7b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x138
-  __DATA.__objc_ivar: 0x50
+  __AUTH.__data: 0x10
+  __DATA.__objc_ivar: 0x54
   __DATA.__data: 0xd4
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF0C493B-42C7-3F9F-8E16-A5B1F4369A2F
-  Functions: 262
-  Symbols:   1331
-  CStrings:  1458
+  UUID: 13423B5D-E6D4-3E47-98CF-B3B67367CDE8
+  Functions: 270
+  Symbols:   1365
+  CStrings:  1490
 
Symbols:
+ +[NSString(MobileActivation) stringWithUTF8StringData:]
+ -[DeviceTypeDeviceIdentity is_factory_restored]
+ -[NSData(MobileActivation) lastByteEqualTo:]
+ -[NSData(MobileActivation) lastByte]
+ -[NSString(MobileActivation) dataFromHexString:]
+ _NSRangeException
+ _OBJC_CLASS_$_NSException
+ _OBJC_IVAR_$_DeviceTypeDeviceIdentity._is_factory_restored
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_MobileActivation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_MobileActivation
+ __OBJC_$_CATEGORY_NSString_$_MobileActivation
+ _gSysctlInterface
+ _isRunningInRecoveryFromSysctl
+ _kMAIsFactoryRestoredOverride
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$dataWithCapacity:
+ _objc_msgSend$lastByte
+ _objc_msgSend$lastByteEqualTo:
+ _objc_msgSend$raise:format:
+ _objc_msgSend$stringWithUTF8StringData:
+ _objc_msgSend$substringFromIndex:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _strtoul
+ _sysctlCopyData
+ _sysctlCopyDataDarwin
CStrings:
+ ""
+ "0"
+ "0x"
+ "4"
+ "@20@0:8I16"
+ "@24@0:8@16"
+ "B20@0:8C16"
+ "C16@0:8"
+ "IsFactoryRestoredOverride"
+ "IsFactorySignedRestore"
+ "TB,R,N,V_is_factory_restored"
+ "_is_factory_restored"
+ "appendBytes:length:"
+ "dataFromHexString:"
+ "dataWithCapacity:"
+ "device-recovery"
+ "hw.osenvironment"
+ "iOS Device Activator (MobileActivation-1076.100.28)"
+ "is_factory_restored"
+ "lastByte"
+ "lastByteEqualTo:"
+ "no valid last byte for data with zero length"
+ "raise:format:"
+ "stringWithUTF8StringData:"
+ "substringFromIndex:"
+ "wirelesseventanalyzerd"
- "$"
- "iOS Device Activator (MobileActivation-1076.100.26)"

```
