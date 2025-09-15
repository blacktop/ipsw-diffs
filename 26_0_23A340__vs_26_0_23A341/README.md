# 26.0 (23A340) .vs 26.0 (23A341)

## IPSWs

- `iPhone17,1_26.0_23A340_Restore.ipsw`
- `iPhone17,1_26.0_23A341_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.0 *(23A340)* | 25.0.0 | 12377.2.8~1 | Tue, 26Aug2025 20:30:59 PDT |
| 26.0 *(23A341)* | 25.0.0 | 12377.2.8~1 | Tue, 26Aug2025 20:30:59 PDT |

## MachO

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### callservicesd

>  `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

-1575.100.1.2.14
-  __TEXT.__text: 0x46b3ec
-  __TEXT.__auth_stubs: 0x4b00
-  __TEXT.__objc_stubs: 0x34ec0
-  __TEXT.__objc_methlist: 0x26ba8
+1575.100.1.2.16
+  __TEXT.__text: 0x46b690
+  __TEXT.__auth_stubs: 0x4b10
+  __TEXT.__objc_stubs: 0x34ee0
+  __TEXT.__objc_methlist: 0x26bb8
   __TEXT.__const: 0xd200
-  __TEXT.__gcc_except_tab: 0x2968
+  __TEXT.__gcc_except_tab: 0x2980
   __TEXT.__cstring: 0x24e0d
-  __TEXT.__objc_methname: 0x60f61
+  __TEXT.__objc_methname: 0x60f8d
   __TEXT.__objc_classname: 0x2db5
   __TEXT.__objc_methtype: 0x107a0
-  __TEXT.__oslogstring: 0x4aab3
+  __TEXT.__oslogstring: 0x4ab63
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x83fa
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__unwind_info: 0xd570
   __TEXT.__eh_frame: 0x8980
-  __DATA_CONST.__auth_got: 0x2590
+  __DATA_CONST.__auth_got: 0x2598
   __DATA_CONST.__got: 0x2408
   __DATA_CONST.__auth_ptr: 0x12e8
-  __DATA_CONST.__const: 0x17d08
+  __DATA_CONST.__const: 0x17ce0
   __DATA_CONST.__cfstring: 0xae40
   __DATA_CONST.__objc_classlist: 0xbf8
   __DATA_CONST.__objc_catlist: 0x140

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x3b638
-  __DATA.__objc_selrefs: 0x12498
+  __DATA.__objc_selrefs: 0x124a0
   __DATA.__objc_ivar: 0x1dcc
   __DATA.__objc_data: 0xd450
   __DATA.__data: 0xf318

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5543B521-38E9-38FC-99DA-F32BB3311F97
-  Functions: 23812
-  Symbols:   2588
-  CStrings:  24965
+  UUID: 7ADABCBA-DF8A-3BE2-A1A4-FDFA8A50E736
+  Functions: 23813
+  Symbols:   2589
+  CStrings:  24970
 
Symbols:
+ _TUDisableCallRelayIDSServiceMessaging
CStrings:
+ "Ending call with receptionistState %lu, reason: %d"
+ "[WARN] call.receptionistState: %d"
+ "_endCallWithActiveReceptionistState:reason:"
+ "not a CSDProviderCall class or not hosted on current device"
+ "receivedInvitationDeclineWithData"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A340)* | iBoot-13822.2.13 |
| 26.0 *(23A341)* | iBoot-13822.2.13 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A340)* | 622.1.22.10.9 |
| 26.0 *(23A341)* | 622.1.22.10.9 |

### Dylibs

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### TelephonyUtilities

>  `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1575.100.1.2.14
-  __TEXT.__text: 0x16ce54
+1575.100.1.2.16
+  __TEXT.__text: 0x16cea0
   __TEXT.__auth_stubs: 0x2370
   __TEXT.__objc_methlist: 0x1a1d8
-  __TEXT.__cstring: 0x13358
+  __TEXT.__cstring: 0x13388
   __TEXT.__const: 0x1044
   __TEXT.__oslogstring: 0x12422
   __TEXT.__gcc_except_tab: 0x18f4

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5d58
+  __TEXT.__unwind_info: 0x5d60
   __TEXT.__eh_frame: 0x1378
   __TEXT.__objc_classname: 0x2727
   __TEXT.__objc_methname: 0x3c217

   __DATA_CONST.__objc_arraydata: 0x6f8
   __AUTH_CONST.__auth_got: 0x11c8
   __AUTH_CONST.__const: 0x3128
-  __AUTH_CONST.__cfstring: 0x11c80
+  __AUTH_CONST.__cfstring: 0x11ca0
   __AUTH_CONST.__objc_const: 0x28268
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 72FDB38E-313B-30C9-8D27-D7BD7D785048
-  Functions: 10019
-  Symbols:   29949
-  CStrings:  16404
+  UUID: F0F3DBE5-94D9-3109-BFF2-33BD38047868
+  Functions: 10020
+  Symbols:   29950
+  CStrings:  16406
 
Symbols:
+ _TUDisableCallRelayIDSServiceMessaging
+ ___block_literal_global.400
+ ___block_literal_global.405
+ ___block_literal_global.410
- ___block_literal_global.397
- ___block_literal_global.402
- ___block_literal_global.407
Functions:
+ _TUDisableCallRelayIDSServiceMessaging
CStrings:
+ "disable-call-relay-idsservice-messaging"

```


</details>

## EOF
