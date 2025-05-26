# 17.0.1 (21A340) .vs 17.0.2 (21A351)

## IPSWs

- `iPhone15,2_17.0.1_21A340_Restore.ipsw`
- `iPhone15,2_17.0.2_21A351_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.0.1 *(21A340)* | 23.0.0 | 10002.2.12~1 | Fri, 15Sep2023 13:43:33 PDT |
| 17.0.2 *(21A351)* | 23.0.0 | 10002.2.12~1 | Fri, 15Sep2023 13:43:33 PDT |

## MachO

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### FinishRestoreFromBackup

>  `/usr/libexec/FinishRestoreFromBackup`

```diff

-1996.2.2.0.0
-  __TEXT.__text: 0x2e0c
+1996.2.3.0.0
+  __TEXT.__text: 0x2e40
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x1684
+  __TEXT.__cstring: 0x169c
   __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__auth_got: 0x260
   __DATA_CONST.__got: 0x48

   - /usr/lib/libSystem.B.dylib
   Functions: 41
   Symbols:   90
-  CStrings:  261
+  CStrings:  262
 
CStrings:
+ "nameSize cannot be zero"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.0.1 *(21A340)* | 616.1.27.10.15 |
| 17.0.2 *(21A351)* | 616.1.27.10.15 |

## EOF
