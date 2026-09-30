## NetAuth

> `/System/Library/PrivateFrameworks/NetAuth.framework/Versions/A/NetAuth`

```diff

 181.0.1.0.0
-  __TEXT.__text: 0xb554
+  __TEXT.__text: 0xb5f0
   __TEXT.__auth_stubs: 0x480
   __TEXT.__cstring: 0x340
   __TEXT.__const: 0x138
-  __TEXT.__unwind_info: 0x280
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0x288
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x540
   __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x718

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
   - /usr/lib/libSystem.B.dylib
-  UUID: C21B1F1D-F71F-3B86-8D74-247C87D7CD63
-  Functions: 223
-  Symbols:   427
+  UUID: 4C86427F-E5FC-3B1B-BE3D-EDC0FFE0416A
+  Functions: 232
+  Symbols:   436
   CStrings:  69
 
Symbols:
+ GetNetAuthUserAgentPort.cold.1
+ NAAuthCredentialsCreate.cold.1
+ NAChangePasswordCreate.cold.1
+ NAConnectionCreate.cold.1
+ NAErrorDialogCreate.cold.1
+ NAProgressCreate.cold.1
+ NASharePickerCreate.cold.1
+ NAShouldConnectCreate.cold.1
+ NAVolumePasswordCreate.cold.1
Functions:
~ _GetNetAuthUserAgentPort : 68 -> 56
~ _NAAuthCredentialsCreate : 124 -> 108
~ _NAChangePasswordCreate : 124 -> 108
~ _NAProgressCreate : 152 -> 136
~ _NASharePickerCreate : 124 -> 108
~ _NAShouldConnectCreate : 124 -> 108
~ _NAErrorDialogCreate : 124 -> 108
~ _NAVolumePasswordCreate : 124 -> 108
~ _NAConnectionCreate : 140 -> 124
~ __NACopyInternetCredentials : 520 -> 516
~ __NASetInternetCredentials : 564 -> 560
~ _NAUA_reply_ShouldConnectDisplayWithOptions : 128 -> 124
~ _NAUA_AuthCredentialsSetOptions : 440 -> 444
~ _NAUA_AuthCredentialsGetCredentials : 496 -> 500
~ _NAUA_AuthCredentialsClose : 364 -> 368
~ _NAUA_ChangePasswordSetOptions : 440 -> 444
~ _NAUA_ChangePasswordGetCredentials : 496 -> 500
~ _NAUA_ChangePasswordClose : 364 -> 368
~ _NAUA_DisplayErrorInfo : 388 -> 392
~ _NAUA_ProgressSetOptions : 440 -> 444
~ _NAUA_ProgressDisplay : 416 -> 420
~ _NAUA_ProgressUpdate : 368 -> 372
~ _NAUA_ProgressClose : 364 -> 368
~ _NAUA_SharePickerSetOptions : 440 -> 444
~ _NAUA_SharePickerGetSelectedShares : 516 -> 520
~ _NAUA_SharePickerClose : 364 -> 368
~ _NAUA_ShouldConnectDisplayWithOptions : 440 -> 444
~ _NAUA_VolumePasswordSetOptions : 440 -> 444
~ _NAUA_VolumePasswordGetCredentials : 496 -> 500
~ _NAUA_VolumePasswordClose : 364 -> 368
~ _NAUA_GetGenericCredentials : 532 -> 536
~ _NAUA_GetInternetCredentials : 536 -> 540
~ _NAUA_SetGenericCredentials : 460 -> 464
~ _NAUA_SetInternetCredentials : 464 -> 468
~ _NAUA_GetKnownServerMarker : 404 -> 408
~ _NAUA_SetKnownServerMarker : 440 -> 444
~ _NAAA_MountURL : 552 -> 556
~ _NAAA_MountURLCancel : 416 -> 420
~ _NAAA_Proxy_OpenSession : 520 -> 524
~ _NAAA_Proxy_EnumerateShares : 504 -> 508
~ _NAAA_Proxy_Mount : 512 -> 516
~ _NAAA_Proxy_CloseSession : 416 -> 420
~ _NAAA_GetCredentials_OpenSession : 520 -> 524
~ _NAAA_GetCredentials_CloseSession : 416 -> 420
~ _NAAA_GetCredentials_ReportError : 504 -> 508
~ _NAAA_GetCredentials_ShowProgress : 500 -> 504
~ _NAAA_reply_Proxy_CloseSession : 128 -> 124
~ _NAAA_reply_GetCredentials_CloseSession : 128 -> 124

```
