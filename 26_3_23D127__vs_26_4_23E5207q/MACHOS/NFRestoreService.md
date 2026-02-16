## NFRestoreService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRestoreService.xpc/NFRestoreService`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0xf18
-  __TEXT.__auth_stubs: 0x2f0
+364.20.0.0.0
+  __TEXT.__text: 0xc24
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x1ac
   __TEXT.__const: 0x78
   __TEXT.__objc_classname: 0x62
   __TEXT.__objc_methname: 0x2b3
   __TEXT.__objc_methtype: 0x15c
-  __TEXT.__cstring: 0x24d
-  __TEXT.__oslogstring: 0x164
+  __TEXT.__cstring: 0x265
+  __TEXT.__oslogstring: 0x10a
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x50
+  __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 88177396-6FEE-3FF0-82F0-5BC640665BA8
+  UUID: 0F05052B-112B-3297-8551-452BE969E018
   Functions: 11
-  Symbols:   67
-  CStrings:  103
+  Symbols:   64
+  CStrings:  106
 
Symbols:
+ __NSConcreteGlobalBlock
+ _objc_release_x26
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
- _class_isMetaClass
- _objc_claimAutoreleasedReturnValue
- _objc_release_x23
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x3
- _objc_retain_x8
- _object_getClass
- _object_getClassName
- _sel_getName
Functions:
~ sub_100000c4c : 968 -> 740
~ sub_100001014 -> sub_100000f30 : 92 -> 96
~ sub_100001118 -> sub_100001038 : 928 -> 736
~ sub_1000014d0 -> sub_100001330 : 320 -> 200
~ sub_100001610 -> sub_1000013f8 : 1332 -> 1112
CStrings:
+ "%s:%i Current user isn't expected"
+ "%s:%i FW is updated with status %d"
+ "%s:%i Fail to run in time, exiting"
+ "%s:%i PID %d (%s) missing entitlement: %s"
+ "%s:%i Received request to update FW with options : %@"
+ "%s:%i Updating FW"
+ "%{public}s:%i Current user isn't expected"
+ "%{public}s:%i FW is updated with status %d"
+ "%{public}s:%i Fail to run in time, exiting"
+ "%{public}s:%i PID %d (%s) missing entitlement: %s"
+ "%{public}s:%i Received request to update FW with options : %@"
+ "%{public}s:%i Updating FW"
+ "-[NFRestoreServiceServer runService:callback:]"
+ "-[NFRestoreServiceServer runService:callback:]_block_invoke"
+ "-[ServiceDelegate listener:shouldAcceptNewConnection:]"
- "%c[%{public}s %{public}s]:%i Current user isn't expected"
- "%c[%{public}s %{public}s]:%i FW is updated with status %d"
- "%c[%{public}s %{public}s]:%i Fail to run in time, exiting"
- "%c[%{public}s %{public}s]:%i PID %d (%s) missing entitlement: %s"
- "%c[%{public}s %{public}s]:%i Received request to update FW with options : %@"
- "%c[%{public}s %{public}s]:%i Updating FW"

```
