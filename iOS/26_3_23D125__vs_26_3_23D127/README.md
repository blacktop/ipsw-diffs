# 26.3 (23D125) .vs 26.3 (23D127)

## IPSWs

- `iPhone18,1_26.3_23D125_Restore.ipsw`
- `iPhone18,1_26.3_23D127_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.3 *(23D125)* | 25.3.0 | 12377.82.2~2 | Mon, 26Jan2026 20:59:54 PST |
| 26.3 *(23D127)* | 25.3.0 | 12377.82.2~2 | Mon, 26Jan2026 20:59:54 PST |

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.3 *(23D125)* | iBoot-13822.82.4 |
| 26.3 *(23D127)* | iBoot-13822.82.4 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.3 *(23D125)* | 623.2.7.10.4 |
| 26.3 *(23D127)* | 623.2.7.10.4 |

### Dylibs

#### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### CallHistory

>  `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

```diff

-106.400.41.2.6
-  __TEXT.__text: 0x1a2a10
+106.400.41.2.7
+  __TEXT.__text: 0x1a2a2c
   __TEXT.__auth_stubs: 0x2460
   __TEXT.__objc_methlist: 0x3a04
   __TEXT.__const: 0x1e5e4

   __TEXT.__unwind_info: 0x6610
   __TEXT.__eh_frame: 0x7888
   __TEXT.__objc_classname: 0x6b4
-  __TEXT.__objc_methname: 0x9b37
+  __TEXT.__objc_methname: 0x9b39
   __TEXT.__objc_methtype: 0x12c3
   __TEXT.__objc_stubs: 0x7840
   __DATA_CONST.__got: 0x978

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9E984E26-C395-39E4-AC4F-0C53EFAE9CED
+  UUID: E917B708-3FB0-3143-97A8-DFCC6116510D
   Functions: 12351
   Symbols:   7799
   CStrings:  3526
Functions:
~ -[CHRecentCall init] : 252 -> 260
~ -[CHRecentCall .cxx_destruct] : 476 -> 488
~ -[CHRecentCall initWithCoder:] : 2320 -> 2324
~ -[CHRecentCall copyWithZone:] : 1052 -> 1056
CStrings:
+ "106.400.41.2.7"
+ "106.400.41.2.7~1"
+ "T@\"NSString\",C,N,V_originatingDeviceName"
- "106.400.41.2.6"
- "106.400.41.2.6~3"
- "T@\"NSString\",N,V_originatingDeviceName"

```

#### SpringBoard

>  `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.3.9.101.0
-  __TEXT.__text: 0xa9d800
+4557.3.9.102.0
+  __TEXT.__text: 0xa9d810
   __TEXT.__auth_stubs: 0x55a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xb8830

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 370371B3-C02B-3032-A678-71B19D395352
+  UUID: 7212C633-68AD-3517-9B45-C0DF6E3DF731
   Functions: 70452
   Symbols:   238272
   CStrings:  104788
Functions:
~ -[SBApplication iconAllowsLaunch:] : 60 -> 28
~ -[SBApplication iconShouldBeDimmed:] : 28 -> 76

```


</details>

## EOF
