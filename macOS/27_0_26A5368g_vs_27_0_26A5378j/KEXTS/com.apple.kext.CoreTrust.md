## com.apple.kext.CoreTrust

> `com.apple.kext.CoreTrust`

```diff

   __TEXT.__const: 0x6b78
-  __TEXT_EXEC.__text: 0xad5c
+  __TEXT_EXEC.__text: 0xad34
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xd8
   __DATA.__common: 0x10
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Functions:
~ _CTCopyDeviceIdentifiers -> _CTConvertAsciiHexToUint64 : 292 -> 332
~ _CTConvertDashTerminatedHexstringTo64BitInteger -> _CTCopyDeviceIdentifiers : 252 -> 292
~ _CTEvaluateBAASystem -> _CTConvertDashTerminatedHexstringTo64BitInteger : 72 -> 252
~ _CTEvaluateBAASystemWithId -> _CTEvaluateBAASystem : 164 -> 72
~ _CTEvaluateBAASystemTestRoot -> _CTFillBAAIdentity : 156 -> 164
~ _CTEvaluateBAAUser -> _CTEvaluateBAASystemTestRoot : 164 -> 156
~ _CTEvaluateBAAUserTestRoot -> _CTEvaluateBAAUser : 156 -> 164
~ _CTEvaluateBAA -> _CTEvaluateBAAAccessory : 196 -> 156
~ _CTGetBAARootType -> _CTEvaluateBAA : 296 -> 196
~ _CTConvertAsciiHexToUint64 -> _CTGetBAASubCAType : 340 -> 296
~ _validateSignerInfo : 2160 -> 2152
~ _CTGetICDPFederationType : 316 -> 288
~ _X509ChainCheckPathWithOptions : 1464 -> 1468

```
