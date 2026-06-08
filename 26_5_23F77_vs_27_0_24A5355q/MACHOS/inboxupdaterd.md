## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

-176.122.1.0.0
-  __TEXT.__text: 0x7e554
-  __TEXT.__auth_stubs: 0x1340
-  __TEXT.__objc_stubs: 0x74c0
-  __TEXT.__objc_methlist: 0x37e4
-  __TEXT.__cstring: 0x457e
-  __TEXT.__objc_methname: 0x773d
-  __TEXT.__objc_classname: 0x5bf
-  __TEXT.__objc_methtype: 0x13c6
-  __TEXT.__const: 0x6f98
-  __TEXT.__oslogstring: 0x87a2
-  __TEXT.__gcc_except_tab: 0x1914
+253.0.0.0.0
+  __TEXT.__text: 0x82f08
+  __TEXT.__auth_stubs: 0x14b0
+  __TEXT.__objc_stubs: 0x7d20
+  __TEXT.__objc_methlist: 0x3b84
+  __TEXT.__cstring: 0x4d5a
+  __TEXT.__objc_methname: 0x801b
+  __TEXT.__objc_classname: 0x5e7
+  __TEXT.__objc_methtype: 0x155a
+  __TEXT.__const: 0xce03
+  __TEXT.__oslogstring: 0x9946
+  __TEXT.__gcc_except_tab: 0x14fc
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1ef0
-  __DATA_CONST.__auth_got: 0x9b0
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xcff0
-  __DATA_CONST.__cfstring: 0x3d00
-  __DATA_CONST.__objc_classlist: 0x150
+  __TEXT.__unwind_info: 0x1d38
+  __DATA_CONST.__const: 0xe368
+  __DATA_CONST.__cfstring: 0x4500
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_intobj: 0x19c8
   __DATA_CONST.__objc_arraydata: 0x4b8
   __DATA_CONST.__objc_arrayobj: 0x5d0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x82c8
-  __DATA.__objc_selrefs: 0x21d0
-  __DATA.__objc_ivar: 0x398
-  __DATA.__objc_data: 0xd20
-  __DATA.__data: 0x1d40
-  __DATA.__bss: 0x138
+  __DATA_CONST.__auth_got: 0xa68
+  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA.__objc_const: 0x8730
+  __DATA.__objc_selrefs: 0x2408
+  __DATA.__objc_ivar: 0x3c4
+  __DATA.__objc_data: 0xe10
+  __DATA.__data: 0x1da8
+  __DATA.__bss: 0x140
   __DATA.__common: 0x28
+  - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E79B6098-25DB-3E0B-8A63-553A4242F193
-  Functions: 3602
-  Symbols:   443
-  CStrings:  3706
+  UUID: BCFBEC45-6B93-3167-BE16-2E63C6720CE5
+  Functions: 3950
+  Symbols:   481
+  CStrings:  4050
 
Symbols:
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_CKContainer
+ _OBJC_CLASS_$_CKRecordID
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSTimeZone
+ _SecRandomCopyBytes
+ ___stderrp
+ _ccaes_gcm_decrypt_mode
+ _ccaes_gcm_encrypt_mode
+ _ccgcm_aad
+ _ccgcm_finalize
+ _ccgcm_init
+ _ccgcm_set_iv
+ _ccgcm_update
+ _cchybridsig_import_pubkey
+ _cchybridsig_lamps13_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_verify_prehashed_with_context
+ _kImg4DecodeAppleSecureBootG2HybridScheme3Sha384IM4C
+ _kImg4DecodeAppleSecureBootG2HybridScheme3Sha384IM4CNoPQC
+ _kImg4DecodeSecureBootG7Rsa4kSha384IM4C
+ _kImg4DecodeSecureBootRsa1kSha1
+ _kImg4DecodeSecureBootRsa3kSha384
+ _kImg4DecodeSecureBootRsa4kSha384AVP
+ _kImg4DecodeSecureBootRsa4kSha384DDI
+ _kSecRandomDefault
+ _kill
+ _malloc_type_calloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _strcmp
+ _strdup
+ _waitpid
- _objc_retain_x28
CStrings:
+ "%@_InBoxUpdate_WiFi-Traffic.pcap"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n"
+ "%{public}@: BT scan start date is set: %{public}@"
+ "-i"
+ "-k"
+ "-w"
+ "/usr/sbin/tcpdump"
+ ">> CryptoHashMethod=%{public}@ CertificateFormat=%{public}@ BootKeyScheme=%{public}@"
+ ">> DisablePQC=%{bool}d UseAVP=%{bool}d UseAVP3=%{bool}d"
+ "@\"<MIBUPersonalizationControllerDelegate>\""
+ "@\"CKContainer\""
+ "@\"CKDatabase\""
+ "@\"MIBUCloudKitHelper\""
+ "@\"MIBUPersonalizationController\""
+ "@32@0:8Q16^@24"
+ "@48@0:8@16@24@32^@40"
+ "@64@0:8@16@24@32@40@48^@56"
+ "@64@0:8@16@24@32@40^@48^@56"
+ "AES GCM decryption completed successfully"
+ "AES GCM encryption completed successfully"
+ "Asset field is not a base64-encoded string, type: %@"
+ "Attempting to fetch record from CloudKit (attempt %d/%d)"
+ "Authentication tag verification failed: %d"
+ "BTScanStartDate"
+ "Cannot schedule RTC alarm wake"
+ "Checking if device has RTC alarm set..."
+ "CollectTCPDumpForWiFi"
+ "Completion handler called after timeout, ignoring results"
+ "Decoded JSON is not a dictionary"
+ "Decoded asset is not a dictionary"
+ "Deconstructed - nonce: %@, ciphertext: %@, tag: %@"
+ "Decrypted data is nil"
+ "Decryption key is nil"
+ "Deleting Personalization..."
+ "Deriving Device Key for Personalization..."
+ "Deriving Personalization Key for decrypting record blob..."
+ "Deriving Personalization Key for record ID..."
+ "Device has RTC alarm set: rtcLPMFlag=%{bool}d rtcAlarmSet=%{bool}d"
+ "Device is booted by RTC alarm: %{public, bool}d, from LPMSU: %{public, bool}d"
+ "Encrypted asset data is empty"
+ "Encrypted data too short: %zu bytes (minimum 28 required)"
+ "Failed to allocate memory for argv."
+ "Failed to allocate memory for argv[%lu]."
+ "Failed to base64 decode the name field"
+ "Failed to compute record ID"
+ "Failed to connect to wifi, error: %@"
+ "Failed to convert record ID data to hex string"
+ "Failed to create personalization info directory: %{public}@"
+ "Failed to decode base64-encoded asset field"
+ "Failed to decrypt asset data"
+ "Failed to decrypt data: %d"
+ "Failed to decrypt personalization record blob"
+ "Failed to decrypt record blob: %@"
+ "Failed to delete personalization info file: %{public}@"
+ "Failed to derive Personalization Device Key"
+ "Failed to derive decryption key: %@"
+ "Failed to derive personalization key for record ID: %@"
+ "Failed to deserialize build version"
+ "Failed to deserialize sep nonce"
+ "Failed to encrypt data: %d"
+ "Failed to fetch record after %d attempts"
+ "Failed to fetch record from CloudKit after %d attempts"
+ "Failed to fetch record on attempt %d/%d"
+ "Failed to finalize GCM: %d"
+ "Failed to find RTC alarm event: %{public}@"
+ "Failed to generate random IV: %d"
+ "Failed to get caches directory"
+ "Failed to get data protection class for given path %s with errno %s (%d)\n"
+ "Failed to get personalization info directory"
+ "Failed to initialize GCM context: %d"
+ "Failed to parse and validate record contents"
+ "Failed to parse asset JSON: %@"
+ "Failed to parse outer JSON: %@"
+ "Failed to process AAD: %d"
+ "Failed to read BT LPM flag: %{public}@"
+ "Failed to read RTC alarm LPM flag: %{public}@"
+ "Failed to read personalization data from plist file"
+ "Failed to read personalization dictionary from file or file is corrupted"
+ "Failed to save personalization data to cache"
+ "Failed to select IMG4 decode implementation. Defaulting to kImg4DecodeSecureBootRsa4kSha384"
+ "Failed to serialize personalization dictionary to plist data: %{public}@"
+ "Failed to set GCM IV: %d"
+ "Failed to write personalization dictionary to file: %{public}@"
+ "Fetch failed: %@"
+ "Fetch timed out after %d seconds"
+ "Handling isRTCAlarmSetWithReply: xpc call"
+ "Handling vendPersonalizationDataIfAvailableWithReply: xpc call"
+ "IODeviceTree:/chosen"
+ "IODeviceTree:/defaults"
+ "Invalid AES key length: %zu"
+ "Invalid IV length: %zu"
+ "Invalid authentication tag length: %zu"
+ "Invalid customer name after decoding"
+ "Invalid or missing 'assetTtlInHrs' in metadata (must be >= 0), got: %@"
+ "Invalid or missing 'language' in metadata"
+ "Invalid or missing 'name' in asset"
+ "Invalid or missing 'orderId' in metadata"
+ "Invalid or missing 'workflowId' in metadata"
+ "Invalid parameters for AES GCM decryption"
+ "Invalid parameters for AES GCM encryption"
+ "Invalid parameters for personalization record blob decryption"
+ "Invalid personalization dictionary provided"
+ "Invalid recordBlob - field is nil or empty"
+ "LPMRTCAlarmWakeDate"
+ "LPMScanStartDate"
+ "MIBUCacheHelper"
+ "MIBUCloudKitHelper"
+ "MIBUPersonalizationController"
+ "MIBUPersonalizationControllerDelegate"
+ "Max SU download retries (%u) reached, failing"
+ "Max SU install retries (%u) reached, failing"
+ "Max SU scan retries (%u) reached, failing"
+ "NP"
+ "No interface provided. Default to en0."
+ "No record found for recordID: %@"
+ "No record provided"
+ "Operation already in progress"
+ "Personalization already completed"
+ "Personalization callback after termination, ignoring"
+ "Personalization controller not running"
+ "Personalization data file not found"
+ "Personalization deletion done with error: %{public}@"
+ "Personalization finished with error: %{public}@"
+ "Personalization info file already did not exist, deletion goal achieved"
+ "Personalization info file does not exist at: %{public}@"
+ "Personalization key derived: %{public}@ use case: %{public}@"
+ "Personalization record blob decryption completed successfully"
+ "PersonalizationName"
+ "RTC alarm wake date must be a future date"
+ "RTC alarm wake must take place before BT scan start"
+ "Record ID data is nil"
+ "Record blob does not contain 'asset' field"
+ "Record blob does not contain valid 'metadata' field"
+ "Record blob is nil or empty"
+ "Record validation failed"
+ "Record validation successful"
+ "Repair UCRT"
+ "Retrying SU install: %lu/%u with delay: %lld (secs)"
+ "Returning personalization data: %{public}@"
+ "Scan start date must be a future date"
+ "Selecting IMG4 decode implementation using parameters:"
+ "Setting LPM parameter 'scanDelayStart' to: %ld"
+ "SkipPersonalizationDeletion"
+ "Skipping personalization deletion"
+ "Software Update cancelled, not starting SU install"
+ "Starting personalization controller..."
+ "Starting tcpdump on interface: %{public}@ Output path: %{public}@"
+ "Stopping tcpdump with PID: %d"
+ "Successfully computed record ID"
+ "Successfully decoded and validated record blob"
+ "Successfully deleted personalization info file at: %{public}@"
+ "Successfully fetched record on attempt %d"
+ "Successfully read personalization data from cache: %{public}@"
+ "Successfully saved personalization dictionary to: %{public}@"
+ "T@\"<MIBUPersonalizationControllerDelegate>\",W,N,V_delegate"
+ "T@\"CKContainer\",&,N,V_container"
+ "T@\"CKDatabase\",&,N,V_database"
+ "T@\"MIBUCloudKitHelper\",&,N,V_ckHelper"
+ "T@\"MIBUPersonalizationController\",&,N,V_personalizationController"
+ "T@\"NSData\",R,N,V_recordBlob"
+ "TB,N,V_running"
+ "TB,N,V_wakedUpByRTCAlarm"
+ "TQ,N,V_installRetry"
+ "Ti,N,V_tcpdumpPID"
+ "Triggering software update install (retry: %lu, cancelled: %d, current phase: %lu)..."
+ "Unsupported record version: %@ (expected: %d)"
+ "Waiting %d seconds before retry..."
+ "WakedByRTCAlarm"
+ "_ckHelper"
+ "_computeRecordID"
+ "_copyCryptoHashMethod"
+ "_copyDeviceTreeString:key:defaultValue:"
+ "_copySecureBootCertificateFormat"
+ "_copySecureBootKeyScheme"
+ "_database"
+ "_decryptDataWithAESGCM:key:iv:additionalData:tag:error:"
+ "_decryptRecordBlob:"
+ "_derivePersonalizationKeyForUseCase:outError:"
+ "_deviceIsAVP"
+ "_deviceIsAVP3"
+ "_encryptDataWithAESGCM:key:iv:additionalData:tag:error:"
+ "_encryptDataWithAESGCMAndRandomIV:key:additionalData:error:"
+ "_fetchRecordWithRetry:"
+ "_getIMG4DecodeImplementation"
+ "_hardwareDisabledPQC"
+ "_installRetry"
+ "_operationDoneWithShutdown:error:"
+ "_parseAndValidateRecordBlob:"
+ "_personalizationController"
+ "_personalizationInfoDirectory"
+ "_recordBlob"
+ "_startTCPDumpOnInterface:"
+ "_stopTCPDump"
+ "_tcpdumpPID"
+ "_validateRecord:"
+ "_wakedUpByRTCAlarm"
+ "asset"
+ "assetTtlInHrs"
+ "chicago"
+ "ckHelper"
+ "collectTCPDumpForWiFi"
+ "com.apple.inboxupdaterd.personalization.v1"
+ "com.apple.mobileinboxupdater.personalization"
+ "container"
+ "containerWithIdentifier:"
+ "crypto-hash-method"
+ "dataWithLength:"
+ "dataWithPropertyList:format:options:error:"
+ "database"
+ "decode_pfk_bulk_data"
+ "decode_pfk_bulk_entry"
+ "decryptPersonalizationRecordBlob:WithKey:error:"
+ "deletePersonalizationFromCache:"
+ "deriveDeviceKeyForPersonalization:"
+ "derivePersonalizationKeyForDecryption:"
+ "derivePersonalizationKeyForRecordID:"
+ "derivePersonalizationKeyFromDeviceKey:forUseCase:withSalt:outError:"
+ "dictionaryWithContentsOfURL:"
+ "earlierDate:"
+ "en0"
+ "enableLPMFlagForBT"
+ "fetchRecordByRecordID:"
+ "fetchRecordWithID:completionHandler:"
+ "generateRandomIV:error:"
+ "hybridscheme3"
+ "i16@0:8"
+ "im4c"
+ "initWithBase64EncodedString:options:"
+ "initWithRecordName:"
+ "installDidStartForUpdate:forRetry:"
+ "installRetry"
+ "isPersonalizationAvailable"
+ "isRTCAlarmSet:"
+ "isRTCAlarmSetWithReply:"
+ "isRTCAlarmWakeScheduled:"
+ "language"
+ "laterDate:"
+ "metadata"
+ "name"
+ "orderId"
+ "personalizationController"
+ "personalizationDoneWithShutdown:error:"
+ "personalizationInfo"
+ "personalization_info.plist"
+ "personalizationrecord"
+ "pktap,%@"
+ "pqc-validation-flags"
+ "publicCloudDatabase"
+ "r^{__Img4DecodeImplementation=^?^?^?^?^{?}^{?}^{?}}16@0:8"
+ "readLPMFlagForBT:"
+ "readLPMFlagForRTCAlarm:"
+ "readPersonalizationDataFromCache:"
+ "recordBlob"
+ "recordid"
+ "rsa1024"
+ "rsa3072"
+ "rsa4096"
+ "savePersonalizationInfoToCache:"
+ "scanDelayStart clamped from %ld to 0xFFFF"
+ "scheduleRTCAlarmWakeOnDate:"
+ "secureboot-certificate-format"
+ "secureboot-key-scheme"
+ "setCkHelper:"
+ "setContainer:"
+ "setDatabase:"
+ "setInstallRetry:"
+ "setPersonalizationController:"
+ "setTcpdumpPID:"
+ "setTimeZone:"
+ "setWakedUpByRTCAlarm:"
+ "skipPersonalizationDeletion"
+ "subdataWithRange:"
+ "systemTimeZone"
+ "tcpdump already started!"
+ "tcpdump already stopped."
+ "tcpdump failed to start: %d; (error: %s)"
+ "tcpdump started with PID: %d"
+ "tcpdumpPID"
+ "timeIntervalSinceDate:"
+ "uses-avp-root-ca"
+ "v20@0:8i16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@?0@\"CKRecord\"8@\"NSError\"16"
+ "v28@0:8@\"SUDescriptor\"16B24"
+ "v28@0:8B16@\"NSError\"20"
+ "v28@0:8B16@20"
+ "vendPersonalizationDataIfAvailableWithReply:"
+ "version"
+ "vmm-present"
+ "wakedByRTCAlarm"
+ "wakedUpByRTCAlarm"
+ "workflowId"
+ "x509"
- "/tmp/su/assets/"
- "/usr/local/bin/"
- "/usr/local/bin/python3"
- "/usr/local/bin/suServer.py"
- ":/chosen"
- "Device is booted from LPMSU: %{public}d"
- "Failed to read LPM flag: %{public}@"
- "IODeviceTree"
- "Max download retries (%u) reached, failing"
- "Max scan retries (%u) reached, failing"
- "Server spawn result: %d; (error: %s); PID = %d"
- "Triggering software update install (cancelled: %d, current phase: %lu)..."
- "Use Python script for loopback server!"
- "UsePythonLoopbackServer"
- "aks_fv_new_sibling_vek"
- "aks_stash_escrow"
- "enableLPMFlag"
- "installDidStartForUpdate:"
- "readLPMFlag:"
- "usePythonLoopbackServer"

```
