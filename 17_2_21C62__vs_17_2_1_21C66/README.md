# 17.2 (21C62) .vs 17.2.1 (21C66)

## IPSWs

- `iPhone16,1_17.2_21C62_Restore.ipsw`
- `iPhone16,1_17.2.1_21C66_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.2 *(21C62)* | 23.2.0 | 10002.60.75.0.3~27 | Sun, 12Nov2023 06:35:58 PST |
| 17.2.1 *(21C66)* | 23.2.0 | 10002.60.75.0.3~27 | Sun, 12Nov2023 06:35:58 PST |

## MachO

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### InCallService

>  `/Applications/InCallService.app/InCallService`

```diff

-2869.300.81.2.3
-  __TEXT.__text: 0x170a28
+2869.300.81.2.4
+  __TEXT.__text: 0x170a44
   __TEXT.__auth_stubs: 0x3c60
   __TEXT.__objc_stubs: 0x26080
   __TEXT.__objc_methlist: 0x10c54

```

#### spotlightknowledged

>  `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

-2274.8.2.0.0
-  __TEXT.__text: 0x755d4
+2274.8.3.0.0
+  __TEXT.__text: 0x7535c
   __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_stubs: 0x7020
-  __TEXT.__objc_methlist: 0x3f84
+  __TEXT.__objc_stubs: 0x7000
+  __TEXT.__objc_methlist: 0x3f7c
   __TEXT.__const: 0x3f8
-  __TEXT.__oslogstring: 0x1b32
-  __TEXT.__gcc_except_tab: 0x616c
-  __TEXT.__cstring: 0x3455
-  __TEXT.__objc_methname: 0x784a
-  __TEXT.__objc_classname: 0x737
+  __TEXT.__oslogstring: 0x1b1e
+  __TEXT.__gcc_except_tab: 0x6188
+  __TEXT.__cstring: 0x3428
+  __TEXT.__objc_methname: 0x7816
+  __TEXT.__objc_classname: 0x734
   __TEXT.__objc_methtype: 0xab1
   __TEXT.__dlopen_cstrs: 0x11c
-  __TEXT.__unwind_info: 0x2710
+  __TEXT.__unwind_info: 0x2700
   __TEXT.__eh_frame: 0x74
   __DATA_CONST.__auth_got: 0x9c0
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x25e8
+  __DATA_CONST.__const: 0x25b8
   __DATA_CONST.__cfstring: 0x3da0
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arrayobj: 0x210
-  __DATA.__objc_const: 0x6770
-  __DATA.__objc_selrefs: 0x1f88
+  __DATA.__objc_const: 0x6738
+  __DATA.__objc_selrefs: 0x1f80
   __DATA.__objc_classrefs: 0x490
   __DATA.__objc_superrefs: 0x260
-  __DATA.__objc_ivar: 0x2a4
+  __DATA.__objc_ivar: 0x2a0
   __DATA.__objc_data: 0x27b0
   __DATA.__data: 0x2d8
   __DATA.__bss: 0x278

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2113
+  Functions: 2106
   Symbols:   440
-  CStrings:  2330
+  CStrings:  2325
 
CStrings:
- "\x011"
- "SKG: starting timer"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "com.apple.spotlight.SpotlightKnowledge.Timer"
- "queue"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.2 *(21C62)* | 617.1.17.10.9 |
| 17.2.1 *(21C66)* | 617.1.17.10.9 |

## EOF
