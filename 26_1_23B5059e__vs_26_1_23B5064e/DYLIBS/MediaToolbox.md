## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3285.8.3.0.0
-  __TEXT.__text: 0xb8abec
+3285.9.1.0.0
+  __TEXT.__text: 0xb8b2d8
   __TEXT.__auth_stubs: 0xb340
   __TEXT.__objc_methlist: 0x2484
   __TEXT.__const: 0x4e4c0
-  __TEXT.__cstring: 0x6acf8
-  __TEXT.__oslogstring: 0x55aff
+  __TEXT.__cstring: 0x6ace7
+  __TEXT.__oslogstring: 0x563d8
   __TEXT.__ustring: 0x23e
   __TEXT.__gcc_except_tab: 0x106c
   __TEXT.__dlopen_cstrs: 0x1c8
-  __TEXT.__unwind_info: 0x133a8
+  __TEXT.__unwind_info: 0x133a0
   __TEXT.__eh_frame: 0x290
   __TEXT.__objc_classname: 0x82d
   __TEXT.__objc_methname: 0x6aba
   __TEXT.__objc_methtype: 0x2901
   __TEXT.__objc_stubs: 0x6100
   __DATA_CONST.__got: 0x38f8
-  __DATA_CONST.__const: 0x23480
+  __DATA_CONST.__const: 0x23490
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 575C9D98-EC59-387F-A215-60A18287A896
-  Functions: 38912
-  Symbols:   100257
-  CStrings:  31625
+  UUID: 9203E259-D4FB-38EB-A412-599FD28F0EA0
+  Functions: 38921
+  Symbols:   100285
+  CStrings:  31631
 
Symbols:
+ _OUTLINED_FUNCTION_860
+ _OUTLINED_FUNCTION_861
+ _fbapspManager_restoreRetimeSampleBufferIfNeeded
+ _fpfs_EnqueuePossibleEndOfMediaData
+ _fpfs_TrackMightRenderMoreAudio
+ _fpfsi_AreAnyOtherTracksOfMediaTypeAwaitingPlayingState
+ _kFigPlaybackItemParameter_MissingAudioEditList
+ _kFigPlaybackItemProperty_MissingAudioEditList
+ _playeroverlap_advanceTimeReached.cold.1
+ _vq_sourceSampleBufferQueue_becameEmpty.cold.1
- _fpfs_StopFeedingTrack.cold.1
- _fpra_moreThanOneActiveConsumerWithoutBandwidthBudget.cold.1
- _itemoverlap_removeTimebaseListener.cold.1
CStrings:
+ " %s: ℹ️ [%{public}@ INFO]: Boss configured to support: %@"
+ " %s: ℹ️ [%{public}@ INFO]: Client has overridden the encryption method to something new. We have changed the key specifier we are requesting for: {\n\tNew encryption method: %@\n\tNew key specifier which will match on this request: %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n}"
+ " %s: ℹ️ [%{public}@ INFO]: Key should live on a remote AirPlay receiver, not here. I'm going to drop my reference to it."
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: Couldn't kick off FigHTTP request; hit error %d"
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: Couldn't send a key request callback to the application; since our handle to communicate with it became NULL!"
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: Couldn't send a key request callback; hit error %d"
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: CustomURL load failed because we should prefer AVContentKeySession"
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: CustomURL-based handling failed with internal error: { %@ }"
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: Failed to kick off CustomURL load due to internal error %d"
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: HTTP-based handling failed with internal error %d"
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: Key session failed to process our key; returning an error: { %@ }"
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: Our CustomURL load threw an error: { %@ }"
+ " %s: ⏮️ [%{public}@ =[RESTARTING REQUEST]=> %{public}@ ATTEMPTED VIA %{public}@]: Remote web server returned %@"
+ " %s: ⏰ [%{public}@ RENEWAL TIMER]: < BEEP BEEP BEEP > Time to renew this key!"
+ " %s: ⏰ [%{public}@ RENEWAL TIMER]: Cancelled for this key"
+ " %s: ⏰ [%{public}@ RENEWAL TIMER]: Scheduled at %@ (%.2f seconds from now)"
+ " %s: ⏱️ [%{public}@ REQUEST TIMER]: < BEEP BEEP BEEP > Request timed out!"
+ " %s: ⏱️ [%{public}@ REQUEST TIMER]: Cancelled"
+ " %s: ⏱️ [%{public}@ REQUEST TIMER]: Key request has %d seconds to complete... starting now!"
+ " %s: ▶️ [%{public}@ =[COMPOUND BOSS SENDING REQUEST]=> CKCBR/%llu]: to %{public}s %{public}@"
+ " %s: ▶️ [%{public}@ =[INITIATING REQUEST]=> %{public}@]"
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Request %s; let's tell the application that helped handle it"
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Request was REDIRECTED to the client-managed boss, sending callback to this interested client: %@"
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Request was SKIPPED, sending callback to this interested client: %@"
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Sending %s key request callback to AVContentKeySession"
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Sending request FAILED callback (error = %ld) to this interested client: %@"
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Sending request FAILURE callback to this interested client"
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Sending request SUCCEEDED callback to this interested client: %@"
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Sending request SUCCESS callback to this interested client"
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Telling the application that a key pointed to by key specifier %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... was updated."
+ " %s: ☎️ [%{public}@ =[CALLBACK]=> %{public}s %p]: Telling the application that the protection status of the content en route to the display has changed"
+ " %s: ⚙️ [%{public}@ =[TRYING REQUEST]=> %{public}@ VIA %{public}@]"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED OBJECT]=> %{public}@]: Boss destroyed: %@"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED OBJECT]=> %{public}@]: Disassociating client-managed boss from its compound boss"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED OBJECT]=> %{public}@]: Disassociating default boss from its compound boss"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED OBJECT]=> %{public}@]: Disassociating key on this group since this group is finalized."
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED OBJECT]=> %{public}@]: Disassociating key request callback handle from invalidating boss"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED OBJECT]=> %{public}@]: Disassociating request on this group since this group is finalized."
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED OBJECT]=> %{public}@]: Disassociating this request from: %@"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED OBJECT]=> %{public}@]: Found and removed this key, associated with key specifier %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ...from: %@"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED OBJECT]=> %{public}@]: This request is being finalized; so it won't service this key anymore"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED REFERENCE]=> %p]: Destroying FairPlay MovieID"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED REFERENCE]=> %p]: Disassociating (and invalidating!) protector on group"
+ " %s: ✂️ [%{public}@ =[DISASSOCIATED REFERENCE]=> %p]: Unlinking client %@ from this request; which is being finalized"
+ " %s: ✅ [%{public}@ =[GOT KEY RESPONSE]=> %{public}@ VIA %{public}@]"
+ " %s: ❌ [%{public}@ =[FAILED REQUEST]=> FOR %{public}@]: Key load FAILED! Error reported: { %@ }"
+ " %s: ❌ [%{public}@ ERROR]: FAILED to create SPC on cryptor %p (error = %d) according to creation options {\n\tKey should have been persistable?: %s\n\tEncryption method: %@\n\tProvided an asset identifier (in addition to an application certificate)?: %s\n\tSupported protocols for key exchange: %@\n\tWould encrypt SPC on behalf of remote AirPlay sender?: %s\n\tReturned key would support buffered AirPlay passthrough?: %s\n\tIncluded a previously acquired key (i.e. synchronous SPC)?: %s\n\tClient requested to randomize the device identifier: %s\n\tClient provided a seed to randomize the device identifier: %s\n}"
+ " %s: ❌ [%{public}@ ERROR]: Failed to complete FigContentKey creation (error = %d) {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n}"
+ " %s: ❌ [%{public}@ ERROR]: Failed to configure for this key (error = %d)"
+ " %s: ❌ [%{public}@ ERROR]: Failed to create FigContentKeyBoss (error = %d)"
+ " %s: ❌ [%{public}@ ERROR]: Failed to create a cryptor (error = %d) with options %@"
+ " %s: ❌ [%{public}@ ERROR]: Failed to create a new FigContentKeyGroup (error = %d) backing: %@"
+ " %s: ❌ [%{public}@ ERROR]: Failed to create a new FigContentKeyRequest (error = %d) against key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n}"
+ " %s: ❌ [%{public}@ ERROR]: Failed to derive persistable key from key response via cryptor %p (error = %d)"
+ " %s: ❌ [%{public}@ ERROR]: Failed to flight request callback to application-layer object %p; error = %d"
+ " %s: ❌ [%{public}@ ERROR]: Failed to flight request callback to interested client %p; error = %d"
+ " %s: ❌ [%{public}@ ERROR]: Failed to process FigContentKeyResponse on cryptor %p (error = %d) {\n\tKey system in play: %@\n\tResponse type: %@\n\tHad an IV attached?: %s\n\tWould have renewal at date: %@\n}"
+ " %s: ❌ [%{public}@ ERROR]: Key request data generation FAILED because the associated request (raw request ID = %llu) was torn down"
+ " %s: ❌ [%{public}@ ERROR]: Key request data generation FAILED because we were unable to generate a key (err = %d)"
+ " %s: ❌ [%{public}@ ERROR]: Key response processing FAILED because the associated request (raw request ID = %llu) was torn down"
+ " %s: 🌱 [%{public}@ CREATED]: FigContentCompoundKeyBoss [%p]"
+ " %s: 🌱 [%{public}@ CREATED]: FigContentKey [%p] {\n\tKey specifier: %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n\t}\n\tLow value key: %s\n\tSupports persistence: %s\n\tIs a preload: %s\n\tKey is doing decryption: %@\n\tDecrypted content will eventually be played back: %@\n}"
+ " %s: 🌱 [%{public}@ CREATED]: FigContentKeyBoss [%p]"
+ " %s: 🌱 [%{public}@ CREATED]: FigContentKeyCompoundBossRequest [%p] {\n\tRequesting a key matching the key specifier: %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n\t}\n\tGroup: %@\n\tWill reuse existing keys from any group: %s\n\tWeak callback client: %p\n}"
+ " %s: 🌱 [%{public}@ CREATED]: FigContentKeyGroup [%p] {\n\tThis is: %@\n\tKeys created under this object support reencryption: %s\n\tApplication audit token: %@\n}"
+ " %s: 🌱 [%{public}@ CREATED]: FigContentKeyRequest [%p] {\n\tRequesting a key matching the key specifier: %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n\t}\n\tBelongs to: %@\n\tIs a renewal request for an existing key?: %s\n\tIs a client-initiated / preload request?: %s\n}"
+ " %s: 🎬 [%{public}@ =[REQUESTED]=> KD Movie ID 0x%llx]: Created a query for the expiration date of a single persistent key: {\n\tPersistable content key data: PROVIDED\n\tNegotiating through FairPlay protocol version 1\n}"
+ " %s: 🎬 [%{public}@ =[REQUESTED]=> KD Movie ID 0x%llx]: Creating a proof of invalidation for ALL PERSISTENT KEYS: {\n\tApplication certificate: PROVIDED\n\tNegotiating through FairPlay protocol version 1\n\tWe received a nonce to use from the client: %s\n}"
+ " %s: 🎬 [%{public}@ =[REQUESTED]=> KD Movie ID 0x%llx]: Creating a proof of invalidation for a single persistent key: {\n\tPersistable content key data: PROVIDED\n\tNegotiating through FairPlay protocol version 1\n\tWe received a nonce to use from the client: %s\n}"
+ " %s: 🏁 [%{public}@ =[COMPLETED REQUEST]=> FOR %{public}@]"
+ " %s: 💥 [%{public}@ FREED]"
+ " %s: 📤 [%{public}@ =[REQUESTED]=> cryptor %p]: Created SPC [%p] according to creation options {\n\tKey should be persistable?: %s\n\tEncryption method: %@\n\tProvided an asset identifier (in addition to an application certificate)?: %s\n\tSupported protocols for key exchange: %@\n\tIs encrypting SPC on behalf of remote AirPlay sender?: %s\n\tReturned key should support buffered AirPlay passthrough?: %s\n\tIncludes a previously acquired key (i.e. synchronous SPC)?: %s\n\tClient requested to randomize the device identifier: %s\n\tClient provided a seed to randomize the device identifier: %s\n}"
+ " %s: 📤 [%{public}@ =[REQUESTED]=> cryptor %p]: Derived persistable key blob %p from key response"
+ " %s: 📤 [%{public}@ =[REQUESTED]=> cryptor %p]: Processed FigContentKeyResponse [%p] on cryptor {\n\tKey system in play: %@\n\tResponse type: %@\n\tHas an IV attached?: %s\n\tShould be renewed at date: %@\n}"
+ " %s: 📩 [cryptor %p =[NOTIFIED]=> %{public}@]: External protection status for this key is currently INSUFFICIENT -- playback should not proceed"
+ " %s: 📩 [cryptor %p =[NOTIFIED]=> %{public}@]: External protection status for this key is currently SUFFICIENT -- playback may proceed"
+ " %s: 📩 [cryptor %p =[NOTIFIED]=> %{public}@]: External protection status for this key is currently unstable -- negotiation is still underway"
+ " %s: 📩 [cryptor %p =[NOTIFIED]=> %{public}@]: Received an updated persistent key blob"
+ " %s: 📲 [API ENTRY => %{public}@]: %{public}s called"
+ " %s: 🔀 [%{public}@ =[REPLACED]=> %{public}@] %{public}@ is replaced due to the assumption of %{public}@, which is owned by AVContentKeySession. Redirecting control flow here."
+ " %s: 🔕 [%{public}@ =[SKIPPED REQUEST]=> FOR %{public}@]: This app has an AVContentKeySession, which is a more appropriate mechanism by which to load this key."
+ " %s: 🔕 [%{public}@ =[SKIPPED REQUEST]=> FOR %{public}@]: This request is already complete."
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Added this key, associated with the specifier %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n} ... to: %@"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Associated a client-managed boss with the compound boss"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Associated a default boss with the compound boss"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Boss created new group"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Created a new protector {\n\tVends cryptors for key system: %@\n\tVends cryptors supporting reencryption: %s\n\tVends cryptors which can protect data sent to a Digital AV adapters: %s\n\tRaw protector creation options: %@\n} ...to vend cryptors for: %@"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: EXISTING FAILED/EXPIRED KEY: A client { %p } wanted this key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... which we previously tried to load but is unusable now. Re-requesting it."
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: EXISTING KEY: A client { %p } wanted this key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... which we found in our cache during request processing. Calling back right away"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: EXISTING REQUEST: A client { %p } wanted this key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... which is already being loaded. Subscribing this client to callbacks on this request"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: KEY RENEWAL: A client { %p } wants to renew this key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... which matches this key. Setting up renewal request for this key"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Migrated this key in %@ owned by the BossFromAsset into %@ owned by the client-managed boss."
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Migrated this request in %@ owned by the BossFromAsset into %@ owned by the client-managed boss."
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Pulling external protection requirement for key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ...off of this key"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Request belongs to this boss."
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Request will be made through: %@"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Using this content key"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: We are asked to revoke a key matching the key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ...and this key matches, so we'll get rid of it."
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Weakly associated key callback recipient with this request"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: Weakly associated requesting client with this request"
+ " %s: 🔗 [%{public}@ =[%{public}s OBJECT]=> %{public}@]: client-managed imported this group [%@] from the bossFromAsset."
+ " %s: 🔗 [%{public}@ =[%{public}s REFERENCE]=> %p]: Associated a new FairPlay movie ID: {\n\tBacked by encrypt method: %@\n\tSupporting protocol versions: %@\n} ... with this boss"
+ " %s: 🔗 [%{public}@ =[%{public}s REFERENCE]=> %p]: Externally provided AirPlay cryptor retained on key; for receiver request ID %llu"
+ " %s: 🔗 [%{public}@ =[%{public}s REFERENCE]=> %p]: New cryptor created on key; with creation options %@"
+ " %s: 🖇️ [%{public}@ =[MERGED INTO]=> %{public}@] %{public}@ is owned by AVContentKeySession, and has thus supplanted the asset's boss %{public}@ in handling requests. All future requests should be redirected to %{public}@"
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s Intro isn't playing yet. introIsWaitingForMixStart:%s. Disconnected rp downstream consumer."
+ "<<<< FigPlayerOverlap >>>> %s: Failed to add timebase listener in intro timebase. with error %d"
+ "<<<< FigPlayerOverlap >>>> %s: Failed to add timebase listener in outro timebase, error %d"
+ "<<<< FigPlayerOverlap >>>> %s: Failed to remove timebase listener from intro timebase with error %d"
+ "<<<< FigPlayerOverlap >>>> %s: Failed to remove timebase listener from outro timebase with error %d"
+ "<<<< FigPlayerOverlap >>>> %s: [player %p|%{public}s] Timebase rate changed from zero to non-zero during outro -- cancelling outro"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: audio track %d format %c%c%c%c missing edit list"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: err=%d track %d has state %d but not feeding render chain. Cannot render sbuf or enqueue to startupQueue"
+ "MissingAudioEditList"
+ "fbapspManager_outputRequiresSubPipeChange"
- " %s: ℹ️ [%@ INFO]: Boss configured to support: %@"
- " %s: ℹ️ [%@ INFO]: Client has overridden the encryption method to something new. We have changed the key specifier we are requesting for: {\n\tNew encryption method: %@\n\tNew key specifier which will match on this request: %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n}"
- " %s: ℹ️ [%@ INFO]: Key should live on a remote AirPlay receiver, not here. I'm going to drop my reference to it."
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: Couldn't kick off FigHTTP request; hit error %d"
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: Couldn't send a key request callback to the application; since our handle to communicate with it became NULL!"
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: Couldn't send a key request callback; hit error %d"
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: CustomURL load failed because we should prefer AVContentKeySession"
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: CustomURL-based handling failed with internal error: { %@ }"
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: Failed to kick off CustomURL load due to internal error %d"
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: HTTP-based handling failed with internal error %d"
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: Key session failed to process our key; returning an error: { %@ }"
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: Our CustomURL load threw an error: { %@ }"
- " %s: ⏮️ [%@ =[RESTARTING REQUEST]=> %@ ATTEMPTED VIA %@]: Remote web server returned %@"
- " %s: ⏰ [%@ RENEWAL TIMER]: < BEEP BEEP BEEP > Time to renew this key!"
- " %s: ⏰ [%@ RENEWAL TIMER]: Cancelled for this key"
- " %s: ⏰ [%@ RENEWAL TIMER]: Scheduled at %@ (%.2f seconds from now)"
- " %s: ⏱️ [%@ REQUEST TIMER]: < BEEP BEEP BEEP > Request timed out!"
- " %s: ⏱️ [%@ REQUEST TIMER]: Cancelled"
- " %s: ⏱️ [%@ REQUEST TIMER]: Key request has %d seconds to complete... starting now!"
- " %s: ▶️ [%@ =[COMPOUND BOSS SENDING REQUEST]=> CKCBR/%llu]: to %s %@"
- " %s: ▶️ [%@ =[INITIATING REQUEST]=> %@]"
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Request %s; let's tell the application that helped handle it"
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Request was REDIRECTED to the client-managed boss, sending callback to this interested client: %@"
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Request was SKIPPED, sending callback to this interested client: %@"
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Sending %s key request callback to AVContentKeySession"
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Sending request FAILED callback (error = %ld) to this interested client: %@"
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Sending request FAILURE callback to this interested client"
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Sending request SUCCEEDED callback to this interested client: %@"
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Sending request SUCCESS callback to this interested client"
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Telling the application that a key pointed to by key specifier %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... was updated."
- " %s: ☎️ [%@ =[CALLBACK]=> %s %p]: Telling the application that the protection status of the content en route to the display has changed"
- " %s: ⚙️ [%@ =[TRYING REQUEST]=> %@ VIA %@]"
- " %s: ✂️ [%@ =[DISASSOCIATED OBJECT]=> %@]: Boss destroyed: %@"
- " %s: ✂️ [%@ =[DISASSOCIATED OBJECT]=> %@]: Disassociating client-managed boss from its compound boss"
- " %s: ✂️ [%@ =[DISASSOCIATED OBJECT]=> %@]: Disassociating default boss from its compound boss"
- " %s: ✂️ [%@ =[DISASSOCIATED OBJECT]=> %@]: Disassociating key on this group since this group is finalized."
- " %s: ✂️ [%@ =[DISASSOCIATED OBJECT]=> %@]: Disassociating key request callback handle from invalidating boss"
- " %s: ✂️ [%@ =[DISASSOCIATED OBJECT]=> %@]: Disassociating request on this group since this group is finalized."
- " %s: ✂️ [%@ =[DISASSOCIATED OBJECT]=> %@]: Disassociating this request from: %@"
- " %s: ✂️ [%@ =[DISASSOCIATED OBJECT]=> %@]: Found and removed this key, associated with key specifier %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ...from: %@"
- " %s: ✂️ [%@ =[DISASSOCIATED OBJECT]=> %@]: This request is being finalized; so it won't service this key anymore"
- " %s: ✂️ [%@ =[DISASSOCIATED REFERENCE]=> %p]: Destroying FairPlay MovieID"
- " %s: ✂️ [%@ =[DISASSOCIATED REFERENCE]=> %p]: Disassociating (and invalidating!) protector on group"
- " %s: ✂️ [%@ =[DISASSOCIATED REFERENCE]=> %p]: Unlinking client %@ from this request; which is being finalized"
- " %s: ✅ [%@ =[GOT KEY RESPONSE]=> %@ VIA %@]"
- " %s: ❌ [%@ =[FAILED REQUEST]=> FOR %@]: Key load FAILED! Error reported: { %@ }"
- " %s: ❌ [%@ ERROR]: FAILED to create SPC on cryptor %p (error = %d) according to creation options {\n\tKey should have been persistable?: %s\n\tEncryption method: %@\n\tProvided an asset identifier (in addition to an application certificate)?: %s\n\tSupported protocols for key exchange: %@\n\tWould encrypt SPC on behalf of remote AirPlay sender?: %s\n\tReturned key would support buffered AirPlay passthrough?: %s\n\tIncluded a previously acquired key (i.e. synchronous SPC)?: %s\n\tClient requested to randomize the device identifier: %s\n\tClient provided a seed to randomize the device identifier: %s\n}"
- " %s: ❌ [%@ ERROR]: Failed to complete FigContentKey creation (error = %d) {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n}"
- " %s: ❌ [%@ ERROR]: Failed to configure for this key (error = %d)"
- " %s: ❌ [%@ ERROR]: Failed to create FigContentKeyBoss (error = %d)"
- " %s: ❌ [%@ ERROR]: Failed to create a cryptor (error = %d) with options %@"
- " %s: ❌ [%@ ERROR]: Failed to create a new FigContentKeyGroup (error = %d) backing: %@"
- " %s: ❌ [%@ ERROR]: Failed to create a new FigContentKeyRequest (error = %d) against key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n}"
- " %s: ❌ [%@ ERROR]: Failed to derive persistable key from key response via cryptor %p (error = %d)"
- " %s: ❌ [%@ ERROR]: Failed to flight request callback to application-layer object %p; error = %d"
- " %s: ❌ [%@ ERROR]: Failed to flight request callback to interested client %p; error = %d"
- " %s: ❌ [%@ ERROR]: Failed to process FigContentKeyResponse on cryptor %p (error = %d) {\n\tKey system in play: %@\n\tResponse type: %@\n\tHad an IV attached?: %s\n\tWould have renewal at date: %@\n}"
- " %s: ❌ [%@ ERROR]: Key request data generation FAILED because the associated request (raw request ID = %llu) was torn down"
- " %s: ❌ [%@ ERROR]: Key request data generation FAILED because we were unable to generate a key (err = %d)"
- " %s: ❌ [%@ ERROR]: Key response processing FAILED because the associated request (raw request ID = %llu) was torn down"
- " %s: 🌱 [%@ CREATED]: FigContentCompoundKeyBoss [%p]"
- " %s: 🌱 [%@ CREATED]: FigContentKey [%p] {\n\tKey specifier: %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n\t}\n\tLow value key: %s\n\tSupports persistence: %s\n\tIs a preload: %s\n\tKey is doing decryption: %@\n\tDecrypted content will eventually be played back: %@\n}"
- " %s: 🌱 [%@ CREATED]: FigContentKeyBoss [%p]"
- " %s: 🌱 [%@ CREATED]: FigContentKeyCompoundBossRequest [%p] {\n\tRequesting a key matching the key specifier: %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n\t}\n\tGroup: %@\n\tWill reuse existing keys from any group: %s\n\tWeak callback client: %p\n}"
- " %s: 🌱 [%@ CREATED]: FigContentKeyGroup [%p] {\n\tThis is: %@\n\tKeys created under this object support reencryption: %s\n\tApplication audit token: %@\n}"
- " %s: 🌱 [%@ CREATED]: FigContentKeyRequest [%p] {\n\tRequesting a key matching the key specifier: %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n\t}\n\tBelongs to: %@\n\tIs a renewal request for an existing key?: %s\n\tIs a client-initiated / preload request?: %s\n}"
- " %s: 🎬 [%@ =[REQUESTED]=> KD Movie ID 0x%llx]: Created a query for the expiration date of a single persistent key: {\n\tPersistable content key data: PROVIDED\n\tNegotiating through FairPlay protocol version 1\n}"
- " %s: 🎬 [%@ =[REQUESTED]=> KD Movie ID 0x%llx]: Creating a proof of invalidation for ALL PERSISTENT KEYS: {\n\tApplication certificate: PROVIDED\n\tNegotiating through FairPlay protocol version 1\n\tWe received a nonce to use from the client: %s\n}"
- " %s: 🎬 [%@ =[REQUESTED]=> KD Movie ID 0x%llx]: Creating a proof of invalidation for a single persistent key: {\n\tPersistable content key data: PROVIDED\n\tNegotiating through FairPlay protocol version 1\n\tWe received a nonce to use from the client: %s\n}"
- " %s: 🏁 [%@ =[COMPLETED REQUEST]=> FOR %@]"
- " %s: 💥 [%@ FREED]"
- " %s: 📤 [%@ =[REQUESTED]=> cryptor %p]: Created SPC [%p] according to creation options {\n\tKey should be persistable?: %s\n\tEncryption method: %@\n\tProvided an asset identifier (in addition to an application certificate)?: %s\n\tSupported protocols for key exchange: %@\n\tIs encrypting SPC on behalf of remote AirPlay sender?: %s\n\tReturned key should support buffered AirPlay passthrough?: %s\n\tIncludes a previously acquired key (i.e. synchronous SPC)?: %s\n\tClient requested to randomize the device identifier: %s\n\tClient provided a seed to randomize the device identifier: %s\n}"
- " %s: 📤 [%@ =[REQUESTED]=> cryptor %p]: Derived persistable key blob %p from key response"
- " %s: 📤 [%@ =[REQUESTED]=> cryptor %p]: Processed FigContentKeyResponse [%p] on cryptor {\n\tKey system in play: %@\n\tResponse type: %@\n\tHas an IV attached?: %s\n\tShould be renewed at date: %@\n}"
- " %s: 📩 [cryptor %p =[NOTIFIED]=> %@]: External protection status for this key is currently INSUFFICIENT -- playback should not proceed"
- " %s: 📩 [cryptor %p =[NOTIFIED]=> %@]: External protection status for this key is currently SUFFICIENT -- playback may proceed"
- " %s: 📩 [cryptor %p =[NOTIFIED]=> %@]: External protection status for this key is currently unstable -- negotiation is still underway"
- " %s: 📩 [cryptor %p =[NOTIFIED]=> %@]: Received an updated persistent key blob"
- " %s: 📲 [API ENTRY => %@]: %s called"
- " %s: 🔀 [%@ =[REPLACED]=> %@] %@ is replaced due to the assumption of %@, which is owned by AVContentKeySession. Redirecting control flow here."
- " %s: 🔕 [%@ =[SKIPPED REQUEST]=> FOR %@]: This app has an AVContentKeySession, which is a more appropriate mechanism by which to load this key."
- " %s: 🔕 [%@ =[SKIPPED REQUEST]=> FOR %@]: This request is already complete."
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Added this key, associated with the specifier %@ {\n\t\tKey system: %@\n\t\tEncrypt method: %@\n\t\tSpecified loading protocols: %@\n} ... to: %@"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Associated a client-managed boss with the compound boss"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Associated a default boss with the compound boss"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Boss created new group"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Created a new protector {\n\tVends cryptors for key system: %@\n\tVends cryptors supporting reencryption: %s\n\tVends cryptors which can protect data sent to a Digital AV adapters: %s\n\tRaw protector creation options: %@\n} ...to vend cryptors for: %@"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: EXISTING FAILED/EXPIRED KEY: A client { %p } wanted this key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... which we previously tried to load but is unusable now. Re-requesting it."
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: EXISTING KEY: A client { %p } wanted this key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... which we found in our cache during request processing. Calling back right away"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: EXISTING REQUEST: A client { %p } wanted this key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... which is already being loaded. Subscribing this client to callbacks on this request"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: KEY RENEWAL: A client { %p } wants to renew this key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ... which matches this key. Setting up renewal request for this key"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Migrated this key in %@ owned by the BossFromAsset into %@ owned by the client-managed boss."
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Migrated this request in %@ owned by the BossFromAsset into %@ owned by the client-managed boss."
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Pulling external protection requirement for key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ...off of this key"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Request belongs to this boss."
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Request will be made through: %@"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Using this content key"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: We are asked to revoke a key matching the key specifier: %@ {\n\tKey system: %@\n\tEncrypt method: %@\n\tSpecified loading protocols: %@\n} ...and this key matches, so we'll get rid of it."
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Weakly associated key callback recipient with this request"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: Weakly associated requesting client with this request"
- " %s: 🔗 [%@ =[%s OBJECT]=> %@]: client-managed imported this group [%@] from the bossFromAsset."
- " %s: 🔗 [%@ =[%s REFERENCE]=> %p]: Associated a new FairPlay movie ID: {\n\tBacked by encrypt method: %@\n\tSupporting protocol versions: %@\n} ... with this boss"
- " %s: 🔗 [%@ =[%s REFERENCE]=> %p]: Externally provided AirPlay cryptor retained on key; for receiver request ID %llu"
- " %s: 🔗 [%@ =[%s REFERENCE]=> %p]: New cryptor created on key; with creation options %@"
- " %s: 🖇️ [%@ =[MERGED INTO]=> %@] %@ is owned by AVContentKeySession, and has thus supplanted the asset's boss %@ in handling requests. All future requests should be redirected to %@"
- "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@]%s Intro isn't playing yet and subpipe manager is shouldFlush=%s. Disconnect rp downstream consumer."
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: err=%d track %d has state %d but no render chain. Cannot render sbuf or enqueue to startupQueue"
- "fbapspManager_outputRequiresSubPipeChangeForHigherFidelity"
- "stream_fix_153761127"

```
