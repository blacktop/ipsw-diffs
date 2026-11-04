## NearFieldPrivateServices

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices`

```diff

-371.8.0.0.0
-  __TEXT.__text: 0x7ef0
-  __TEXT.__objc_methlist: 0x64c
-  __TEXT.__const: 0x98
+372.4.1.0.0
+  __TEXT.__text: 0x8400
+  __TEXT.__objc_methlist: 0x5f4
+  __TEXT.__const: 0xa0
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__cstring: 0x17d9
-  __TEXT.__oslogstring: 0x6e4
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__cstring: 0x1774
+  __TEXT.__oslogstring: 0x6ab
+  __TEXT.__unwind_info: 0x250
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x4d8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__got: 0xb8
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x9a0
+  __DATA_CONST.__got: 0xb0
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__objc_const: 0x9f8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x2c
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x180
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 130
-  Symbols:   122
+  Symbols:   116
   CStrings:  274
 
Symbols:
- __os_activity_create
- __os_activity_current
- _dispatch_once
- _dispatch_sync
- _os_activity_scope_enter
- _os_activity_scope_leave
CStrings:
+ "%s:%i Activate connection"
+ "%s:%i Dispatch work queue is nil"
+ "%s:%i Endpoint is nil"
+ "%s:%i Endpoint=%{public}@"
+ "%{public}s:%i Activate connection"
+ "%{public}s:%i Dispatch work queue is nil"
+ "%{public}s:%i Endpoint is nil"
+ "%{public}s:%i Endpoint=%{public}@"
+ "-[NFBSClient _activate]"
+ "-[NFBSClient _onInvalidation:]"
+ "-[NFBSClient initWithRemoteInterface:]"
+ "-[NFBSClient remoteTarget]"
+ "BSServiceQuality"
+ "Version"
- "%s:%i Endpoint error"
- "%s:%i Endpoint=%{public}@, connection=%{public}@"
- "%s:%i Reactivate connection"
- "%{public}s:%i Endpoint error"
- "%{public}s:%i Endpoint=%{public}@, connection=%{public}@"
- "%{public}s:%i Reactivate connection"
- "-[NFBSClient_BackgroundTagReading _activate]"
- "-[NFBSClient_BackgroundTagReading _onInvalidation:]"
- "-[NFBSClient_BackgroundTagReading remoteTarget]"
- "-[NFBSClient_BackgroundTagReading remoteTarget]_block_invoke"
- "BackgroundTagReadingClient activate"
- "BackgroundTagReadingClient invalidate"
- "com.apple.nfc.background.tag.reading_XPC"
- "unavailable"
```
