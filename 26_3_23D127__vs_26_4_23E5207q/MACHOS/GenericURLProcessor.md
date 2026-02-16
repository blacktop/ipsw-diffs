## GenericURLProcessor

> `/System/Library/ExtensionKit/Extensions/GenericURLProcessor.appex/GenericURLProcessor`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0x2c94
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x380
+364.20.0.0.0
+  __TEXT.__text: 0x2aa8
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_stubs: 0x440
   __TEXT.__objc_methlist: 0x1bc
   __TEXT.__const: 0x200
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x349
-  __TEXT.__objc_methname: 0x46a
+  __TEXT.__objc_classname: 0xbf
+  __TEXT.__objc_methname: 0x419
+  __TEXT.__objc_methtype: 0x1f6
   __TEXT.__constg_swiftt: 0xc0
   __TEXT.__swift5_typeref: 0x116
   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__oslogstring: 0x313
+  __TEXT.__oslogstring: 0x28c
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__objc_classname: 0x8d
-  __TEXT.__objc_methtype: 0x1bf
+  __TEXT.__cstring: 0x403
   __TEXT.__swift5_protos: 0x4
   __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__auth_got: 0x260
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x508
-  __DATA.__objc_selrefs: 0x1d8
+  __DATA.__objc_selrefs: 0x1c8
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x2b8
+  __DATA.__data: 0x2c0
   __DATA.__bss: 0x180
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 025E7F6D-84AC-3316-A445-4607CEC2C948
+  UUID: 4186EAE0-ECC9-3060-A5EE-BC0538D46C26
   Functions: 42
-  Symbols:   137
-  CStrings:  141
+  Symbols:   134
+  CStrings:  144
 
Symbols:
+ __NSConcreteGlobalBlock
+ ___chkstk_darwin
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x27
- _class_isMetaClass
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x9
- _object_getClass
- _object_getClassName
- _sel_getName
Functions:
~ sub_100001580 : 232 -> 220
~ sub_1000019e0 -> sub_1000019d4 : 380 -> 556
~ sub_100001b5c -> sub_100001c00 : 312 -> 480
~ sub_100001c94 -> sub_100001de0 : 368 -> 544
~ sub_100001ec4 -> sub_1000020c0 : 1172 -> 1268
~ sub_100002498 -> sub_1000026f4 : 320 -> 312
~ sub_1000025d8 -> sub_10000282c : 520 -> 528
~ sub_100002924 -> sub_100002b80 : 788 -> 664
~ sub_100002c38 -> sub_100002e18 : 1344 -> 1016
~ sub_100003178 -> sub_100003210 : 468 -> 340
~ sub_100003390 -> sub_1000033a8 : 1028 -> 956
~ sub_100003794 -> sub_100003764 : 224 -> 204
~ sub_100003874 -> sub_100003830 : 880 -> 668
~ sub_100003bf8 -> sub_100003ae0 : 1564 -> 1352
CStrings:
+ "%s:%i Creating barcode parser"
+ "%s:%i Failed to allocate barcode parser"
+ "%s:%i Found AMS Accessory: %{public}@"
+ "%s:%i Found App URL: %@, Orig msg: %@"
+ "%s:%i Maximum retry count is reached; dropping notification"
+ "%s:%i Posted notification, isActionable:%{public}@, error:%{public}@"
+ "%s:%i Posting Wallet Tag notification with UID : %{public}@"
+ "%s:%i Resource error; dropping notification"
+ "%s:%i error=%{public}@"
+ "%{public}s:%i Creating barcode parser"
+ "%{public}s:%i Failed to allocate barcode parser"
+ "%{public}s:%i Found AMS Accessory: %{public}@"
+ "%{public}s:%i Found App URL: %@, Orig msg: %@"
+ "%{public}s:%i Maximum retry count is reached; dropping notification"
+ "%{public}s:%i Posted notification, isActionable:%{public}@, error:%{public}@"
+ "%{public}s:%i Posting Wallet Tag notification with UID : %{public}@"
+ "%{public}s:%i Resource error; dropping notification"
+ "%{public}s:%i error=%{public}@"
+ "-[NFTagAppLauncher processNDEFMesssage:outputMessage:tag:stopProcessing:]"
+ "-[NFTagAppLauncher processTag:withNDEFMessage:matchedProcessor:]"
+ "-[NFTagAppLauncher processTag:withNDEFMessage:matchedProcessor:]_block_invoke"
+ "-[NFTagAppProcessorAMSAccessory processNDEFMesssage:outputMessage:tag:stopProcessing:]"
+ "-[NFTagAppProcessorWallet notifySharingServicesClient:payload:retryCount:]_block_invoke"
+ "-[NFTagAppProcessorWallet processNDEFMesssage:outputMessage:tag:stopProcessing:]"
- "%c[%{public}s %{public}s]:%i Creating barcode parser"
- "%c[%{public}s %{public}s]:%i Failed to allocate barcode parser"
- "%c[%{public}s %{public}s]:%i Found AMS Accessory: %{public}@"
- "%c[%{public}s %{public}s]:%i Found App URL: %@, Orig msg: %@"
- "%c[%{public}s %{public}s]:%i Maximum retry count is reached; dropping notification"
- "%c[%{public}s %{public}s]:%i Posted notification, isActionable:%{public}@, error:%{public}@"
- "%c[%{public}s %{public}s]:%i Posting Wallet Tag notification with UID : %{public}@"
- "%c[%{public}s %{public}s]:%i Resource error; dropping notification"
- "%c[%{public}s %{public}s]:%i error=%{public}@"
- "notifySharingServicesClient:payload:retryCount:"
- "processTag:withNDEFMessage:matchedProcessor:"

```
