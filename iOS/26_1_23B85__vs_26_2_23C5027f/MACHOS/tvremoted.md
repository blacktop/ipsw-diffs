## tvremoted

> `/usr/libexec/tvremoted`

```diff

-548.10.24.0.0
-  __TEXT.__text: 0x1081c
+548.20.7.0.0
+  __TEXT.__text: 0x10898
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x2500
   __TEXT.__objc_methlist: 0xef0
   __TEXT.__const: 0xda
-  __TEXT.__oslogstring: 0x267c
+  __TEXT.__oslogstring: 0x268c
   __TEXT.__cstring: 0x83e
   __TEXT.__gcc_except_tab: 0x1c4
   __TEXT.__objc_methname: 0x3147

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 292C210A-9585-347E-B946-1673235563D8
+  UUID: E0B7ADB7-5816-32DD-B153-35017A2D1882
   Functions: 314
   Symbols:   2369
   CStrings:  947
Functions:
~ ___48-[TVRDServer clientConnectionSeveredConnection:]_block_invoke : 248 -> 244
~ -[TVRDServer device:disconnectedForReason:error:] : 888 -> 924
~ -[TVRDServer _lostInterestInDeviceWithIdentifier:] : 560 -> 652
CStrings:
+ "Added new %{public}@. Total connections: %{public}@"
+ "Removed %{public}@. Total connections: %{public}@"
+ "Updated cachedDevices: %{public}@"
- "Added new %{public}@. Total connections: %@"
- "Removed %{public}@. Total connections: %ld"
- "Updated cachedDevices:%{public}@"

```
