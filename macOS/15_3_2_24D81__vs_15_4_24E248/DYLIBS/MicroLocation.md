## MicroLocation

> `/System/Library/PrivateFrameworks/MicroLocation.framework/Versions/A/MicroLocation`

```diff

-27.0.28.0.4
-  __TEXT.__text: 0xe58c
+27.0.28.0.6
+  __TEXT.__text: 0xe348
   __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0xef8
+  __TEXT.__objc_methlist: 0x11bc
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__gcc_except_tab: 0x160
   __TEXT.__cstring: 0x1930
   __TEXT.__oslogstring: 0x736
-  __TEXT.__unwind_info: 0x430
+  __TEXT.__unwind_info: 0x438
   __TEXT.__objc_classname: 0x1a8
   __TEXT.__objc_methname: 0x270b
   __TEXT.__objc_methtype: 0x698

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x760
+  __DATA_CONST.__objc_selrefs: 0x7e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
   __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__const: 0x3b0
   __AUTH_CONST.__cfstring: 0x1680
-  __AUTH_CONST.__objc_const: 0x1eb0
+  __AUTH_CONST.__objc_const: 0x1980
   __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0xd4
   __DATA.__data: 0x250

   - /System/Library/PrivateFrameworks/MicroLocationUtilities.framework/Versions/A/MicroLocationUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B680796-C538-3CB1-B0C2-571FFD91557C
-  Functions: 376
-  Symbols:   941
+  UUID: 9A4D5F5C-11CF-37DB-9DE1-CC56A7EF06FB
+  Functions: 378
+  Symbols:   977
   CStrings:  914
 
Symbols:
+ +[ULConnection createServiceWithServiceType:locationTypes:reply:].cold.1
+ +[ULConnection deleteServiceWithIdentifier:reply:].cold.1
+ +[ULConnection(Diagnostic) exportDatabaseWithReply:].cold.1
+ +[ULConnection(Diagnostic) purgeDatabaseWithReply:].cold.1
+ +[ULConnection(Diagnostic) queryServicesWithReply:].cold.1
+ +[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:].cold.1
+ +[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:].cold.1
+ +[ULConnection(Legacy) getMicroLocationInternalVersion].cold.1
+ +[ULConnection(Legacy) getMicroLocationInternalVersion].cold.2
+ +[ULConnection(Legacy) getRecordingTriggerUUIDAndRequestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:handler:].cold.1
+ +[ULConnection(Legacy) requestCurrentMicroLocationWithAdditionalInformation:].cold.1
+ -[ULConnection _checkAndRecoverIfNeeded].cold.1
+ -[ULConnection _performAsyncOnDelegateQueueIfRespondsToSelector:block:].cold.1
+ -[ULConnection _xpcInterruptionHandler].cold.2
+ -[ULConnection _xpcInvalidationHandler].cold.2
+ -[ULConnection enableMicrolocationAtCurrentLocation].cold.1
+ _CLLogObjectForCategory_MicroLocation_Default.cold.1
+ __109+[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:]_block_invoke_2.cold.1
+ __138+[ULConnection(Legacy) getRecordingTriggerUUIDAndRequestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:handler:]_block_invoke_2.cold.1
+ __23-[ULConnection connect]_block_invoke.cold.1
+ __26-[ULConnection disconnect]_block_invoke.cold.1
+ __28-[ULConnection stopUpdating]_block_invoke.cold.1
+ __33-[ULConnection requestPrediction]_block_invoke.cold.1
+ __34-[ULConnection requestObservation]_block_invoke.cold.1
+ __47-[ULConnection startUpdatingWithConfiguration:]_block_invoke.cold.1
+ __50+[ULConnection deleteServiceWithIdentifier:reply:]_block_invoke_2.cold.1
+ __51+[ULConnection(Diagnostic) purgeDatabaseWithReply:]_block_invoke_2.cold.1
+ __51+[ULConnection(Diagnostic) queryServicesWithReply:]_block_invoke_2.cold.1
+ __51-[ULConnection initWithDelegate:serviceIdentifier:]_block_invoke.cold.1
+ __52+[ULConnection(Diagnostic) exportDatabaseWithReply:]_block_invoke_2.cold.1
+ __52-[ULConnection(Diagnostic) requestAllModelsLearning]_block_invoke.cold.1
+ __59-[ULConnection labelRequestIdentifier:withPlaceIdentifier:]_block_invoke.cold.1
+ __66-[ULConnection _manageConnectionAvailableNotificationObservation:]_block_invoke_2.cold.1
+ __70-[ULConnection enableMicrolocationAtCurrentLocationWithConfiguration:]_block_invoke.cold.1
+ __73-[ULConnection(Diagnostic) disableMicrolocationAtlocationWithIdentifier:]_block_invoke.cold.1
+ __98+[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:]_block_invoke_2.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationFramework/src/ULConnection.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationFramework/src/ULConnection.m"

```
