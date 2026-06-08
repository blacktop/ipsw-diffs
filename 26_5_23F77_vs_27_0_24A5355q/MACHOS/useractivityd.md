## useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

-606.5.2.0.0
-  __TEXT.__text: 0x803c4
-  __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_stubs: 0xc080
+625.0.0.0.0
+  __TEXT.__text: 0x77a84
+  __TEXT.__auth_stubs: 0xe90
+  __TEXT.__objc_stubs: 0xc000
   __TEXT.__objc_methlist: 0x68bc
   __TEXT.__const: 0x328
-  __TEXT.__cstring: 0x470b
-  __TEXT.__objc_classname: 0xc8d
-  __TEXT.__objc_methname: 0xf877
+  __TEXT.__cstring: 0x4767
+  __TEXT.__objc_classname: 0xc10
+  __TEXT.__objc_methname: 0xf81b
   __TEXT.__objc_methtype: 0x2244
-  __TEXT.__gcc_except_tab: 0xacfc
-  __TEXT.__oslogstring: 0xdc81
+  __TEXT.__gcc_except_tab: 0xa0b0
+  __TEXT.__oslogstring: 0xdbcc
   __TEXT.__dof_UA: 0xfad
-  __TEXT.__unwind_info: 0x2540
-  __DATA_CONST.__auth_got: 0x750
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__auth_ptr: 0x28
+  __TEXT.__unwind_info: 0x2518
   __DATA_CONST.__const: 0x1890
-  __DATA_CONST.__cfstring: 0x5840
+  __DATA_CONST.__cfstring: 0x5800
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100

   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_doubleobj: 0xd0
   __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__auth_got: 0x760
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0xf1e0
-  __DATA.__objc_selrefs: 0x3928
+  __DATA.__objc_selrefs: 0x3908
   __DATA.__objc_ivar: 0x8e8
   __DATA.__objc_data: 0x1b80
   __DATA.__data: 0xc58

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 627F3153-C8C1-3D9F-BAD1-3CC889D54E82
+  UUID: FFC1C71C-D2DC-3B05-A377-95C5B6F683AE
   Functions: 2341
-  Symbols:   402
-  CStrings:  5564
+  Symbols:   401
+  CStrings:  5551
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
- _BRGetCloudEnabledStatus
- _BRHandoffDidReceiveApplicationContinuity
- _OBJC_CLASS_$_NSURLComponents
- __UAUserActivityDidContinueToAppStoreApplicationIdentifierKey
- __UAUserActivityDidContinueToAppStoreNotification
CStrings:
+ "01:02:00"
+ "01:02:25"
+ "IDLE: screen dimmed:%{BOOL}d, deviceUILocked:%{BOOL}d, useractive: %{BOOL}d"
+ "May 23 2026"
+ "Mirroring state changed, updating isUserActive with isMirroringActive %{BOOL}d and screenDimState with %{BOOL}d"
+ "Returned from back to client to ask it to save activity %{public}@, clean=%{BOOL}d updatedInfo=%{private}@"
- "--- Ignoring incoming advertisement because it contains cloud documents, but BRGetCloudEnabledStatus() returned %ld, %{public}@"
- "20:32:15"
- "20:32:37"
- "Apr 18 2026"
- "Error when nudging cloud docs for bundleIdentifier=%{private}@, err=%{public}@"
- "IDLE: screen dimmed: %s, deviceUILocked: %s, useractive: %s"
- "Mirroring state changed, updating isUserActive with isMirroringActive %s and screenDimState with %s"
- "Returned from back to client to ask it to save activity %{public}@, clean=%{public}s updatedInfo=%{private}@"
- "com.apple.AppStore"
- "ids"
- "initWithURL:resolvingAgainstBaseURL:"
- "no"
- "postNotificationName:object:userInfo:"
- "queryItems"
- "value"
- "yes"

```
