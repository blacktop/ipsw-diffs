## NFStorageServer

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFStorageServer.xpc/NFStorageServer`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0xe64
-  __TEXT.__auth_stubs: 0x1d0
+364.20.0.0.0
+  __TEXT.__text: 0xd68
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x19c
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x123
-  __TEXT.__oslogstring: 0x7a
+  __TEXT.__cstring: 0x154
+  __TEXT.__oslogstring: 0x5c
   __TEXT.__objc_classname: 0x59
   __TEXT.__objc_methname: 0x3a9
   __TEXT.__objc_methtype: 0x156
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x18

   - /usr/lib/libnfshared.dylib
   - /usr/lib/libnfstorage.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CEBEE553-3256-3109-ABF5-29254F0F8B11
+  UUID: 965C21CE-A227-3F74-A069-4EE30AFFD7D0
   Functions: 7
-  Symbols:   47
-  CStrings:  108
+  Symbols:   39
+  CStrings:  110
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _class_isMetaClass
- _objc_claimAutoreleasedReturnValue
- _objc_release_x25
- _objc_retain
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
- _object_getClass
- _object_getClassName
- _sel_getName
CStrings:
+ "%s:%i Got message %@ for model %@"
+ "%s:%i PID %d (%s) missing entitlement: %s"
+ "%{public}s:%i Got message %@ for model %@"
+ "%{public}s:%i PID %d (%s) missing entitlement: %s"
+ "-[NFStorageServer runService:callback:]"
+ "-[ServiceDelegate listener:shouldAcceptNewConnection:]"
- "%c[%{public}s %{public}s]:%i Got message %@ for model %@"
- "%c[%{public}s %{public}s]:%i PID %d (%s) missing entitlement: %s"

```
