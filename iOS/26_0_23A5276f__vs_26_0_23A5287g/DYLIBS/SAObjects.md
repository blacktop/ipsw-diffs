## SAObjects

> `/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects`

```diff

-3500.35.1.0.0
-  __TEXT.__text: 0x3e938
+3500.37.1.0.0
+  __TEXT.__text: 0x3e984
   __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x32098
+  __TEXT.__objc_methlist: 0x320f0
   __TEXT.__const: 0x9c8
-  __TEXT.__cstring: 0x162b6
-  __TEXT.__unwind_info: 0x39a0
+  __TEXT.__cstring: 0x162d3
+  __TEXT.__unwind_info: 0x39e8
   __TEXT.__objc_classname: 0x8bd2
-  __TEXT.__objc_methname: 0x2a0d2
+  __TEXT.__objc_methname: 0x2a09b
   __TEXT.__objc_methtype: 0x49d
   __TEXT.__objc_stubs: 0xf00
   __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0xf9f0
+  __DATA_CONST.__const: 0xfa20
   __DATA_CONST.__objc_classlist: 0x2de8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf1d0
+  __DATA_CONST.__objc_selrefs: 0xf1c0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x2e120
-  __AUTH_CONST.__objc_const: 0x58f50
+  __AUTH_CONST.__cfstring: 0x2e140
+  __AUTH_CONST.__objc_const: 0x58fa0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x16120
   __DATA.__objc_ivar: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 520FB94B-B735-32B8-AED4-5024227F428C
-  Functions: 14925
-  Symbols:   49553
+  UUID: D8F4190A-888B-39A7-AC0E-456D29F40378
+  Functions: 14933
+  Symbols:   49574
   CStrings:  21384
 
Symbols:
+ -[SASResultCandidate setSharedUserId:]
+ -[SASResultCandidate setSpeechId:]
+ -[SASResultCandidate setUserIdentityClassification:]
+ -[SASResultCandidate setVoiceIDConfidenceScores:]
+ -[SASResultCandidate sharedUserId]
+ -[SASResultCandidate speechId]
+ -[SASResultCandidate userIdentityClassification]
+ -[SASResultCandidate voiceIDConfidenceScores]
+ -[SAStartLocalRequest inputOrigin]
+ -[SAStartLocalRequest setInputOrigin:]
+ _SAInputOriginPresentedResponseInteractionValue
+ _SASResultCandidateSharedUserIdPListKey
+ _SASResultCandidateSpeechIdPListKey
+ _SASResultCandidateUserIdentityClassificationPListKey
+ _SASResultCandidateVoiceIDConfidenceScoresPListKey
+ _SAStartLocalRequestInputOriginPListKey
- +[SASResultCandidate resultCandidateWithDictionary:context:]
- +[SASResultCandidate resultCandidate]
- __OBJC_$_CLASS_METHODS_SASResultCandidate
CStrings:
+ "PresentedResponseInteraction"
- "resultCandidate"
- "resultCandidateWithDictionary:context:"

```
