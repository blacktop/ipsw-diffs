## Diagnostic-8340

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`

```diff

 696.140.2.0.0
-  __TEXT.__text: 0x3494
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0x5c0
+  __TEXT.__text: 0xbff8
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_stubs: 0x860
   __TEXT.__objc_methlist: 0x2fc
-  __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x42e
-  __TEXT.__oslogstring: 0x4dc
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x1836
+  __TEXT.__oslogstring: 0xaa7
   __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x8c7
+  __TEXT.__objc_methname: 0x9f4
   __TEXT.__objc_methtype: 0x147
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x3c0
+  __TEXT.__gcc_except_tab: 0x2b4
+  __TEXT.__unwind_info: 0x208
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__cfstring: 0xf80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x198
   __DATA.__objc_const: 0x560
-  __DATA.__objc_selrefs: 0x2d8
+  __DATA.__objc_selrefs: 0x330
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
-  __DATA.__common: 0x10
-  __DATA.__bss: 0x10
+  __DATA.__data: 0x180
+  __DATA.__common: 0x28
+  __DATA.__bss: 0x38
+  - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  UUID: E5369E69-2FB0-3D99-811C-FB6B49653239
-  Functions: 83
-  Symbols:   91
-  CStrings:  281
+  UUID: 3DCC47BE-6B10-3806-BB57-76802AA1011B
+  Functions: 258
+  Symbols:   197
+  CStrings:  644
 
Symbols:
+ _AMAuthInstallApImg4SetSepNonce
+ _AMAuthInstallSetSigningServerURL
+ _AMFDRSealingMapGetFDRDataVersionForDevice
+ _AMSupportCopyHexStringFromData
+ _AMSupportCreateSetFromCFIndexArray
+ _AMSupportHttpCopyProxySettings
+ _AMSupportHttpSendSync
+ _AMSupportLogDumpMemory
+ _AMSupportLogInternal
+ _AMSupportLogSetHandler
+ _CFDataCreate
+ _CFDataCreateCopy
+ _CFDataCreateWithBytesNoCopy
+ _CFDataGetBytePtr
+ _CFDataGetBytes
+ _CFDataGetLength
+ _CFDataGetTypeID
+ _CFDictionaryAddValue
+ _CFDictionaryContainsKey
+ _CFDictionaryCreateCopy
+ _CFDictionaryCreateMutable
+ _CFDictionaryGetTypeID
+ _CFDictionaryGetValue
+ _CFDictionarySetValue
+ _CFErrorCreate
+ _CFGetTypeID
+ _CFHTTPMessageCopyAllHeaderFields
+ _CFHTTPMessageCreateRequest
+ _CFHTTPMessageSetBody
+ _CFHTTPMessageSetHeaderFieldValue
+ _CFNumberCreate
+ _CFPropertyListCreateData
+ _CFPropertyListCreateWithData
+ _CFRelease
+ _CFRetain
+ _CFStringAppend
+ _CFStringCompare
+ _CFStringCreateMutable
+ _CFStringCreateMutableCopy
+ _CFStringCreateWithFormat
+ _CFStringGetCStringPtr
+ _CFStringGetTypeID
+ _CFURLCreateWithString
+ _CFUUIDCreate
+ _CFUUIDCreateString
+ _HSCGetPearlNonce
+ _HSCSecurePairPearl
+ _HSCSecurePairPearlWithProxy
+ _IOConnectCallMethod
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ _OBJC_CLASS_$_CRPersonalizationManager
+ _OBJC_CLASS_$_CRPreflightController
+ _OBJC_CLASS_$_NSNumber
+ _SavageUpdaterCreate
+ _SavageUpdaterExecCommand
+ _SavageUpdaterIsDone
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___chkstk_darwin
+ ___objc_personality_v0
+ ___stdoutp
+ __logHandler
+ _bzero
+ _ccder_blob_decode_len
+ _ccder_blob_decode_range
+ _ccder_blob_decode_sequence_tl
+ _ccder_blob_decode_tag
+ _ccder_blob_decode_tl
+ _ccder_blob_encode_body
+ _ccder_blob_encode_tl
+ _ccder_sizeof
+ _ccdigest
+ _ccsha384_di
+ _dispatch_queue_create
+ _dispatch_sync
+ _kAMSupportHttpOptionDisableSSLValidation
+ _kAMSupportHttpOptionMaxAttempts
+ _kAMSupportHttpOptionSocksProxySettings
+ _kAMSupportHttpOptionTimeout
+ _kAMSupportHttpOptionValidResponses
+ _kCFAllocatorMalloc
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kCFErrorLocalizedDescriptionKey
+ _kCFHTTPVersion1_1
+ _kCFNull
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _malloc
+ _malloc_type_calloc
+ _malloc_type_malloc
+ _memcmp
+ _memcpy
+ _memset_s
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_release_x10
+ _objc_release_x26
+ _objc_release_x9
+ _objc_retain
+ _objc_retainBlock
+ _pearlSeaCookieHandleMessage
+ _qsort
+ _syslog
CStrings:
+ "\terrorCode: "
+ "\terrorString: "
+ "%.*s"
+ "%.2X"
+ "%@\n"
+ "%d"
+ "%lu"
+ "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
+ "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
+ "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
+ "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
+ "%s: %s"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || message"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || messageLength"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || reply"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || replySize"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize"
+ "*replySize >= outData->dataSize"
+ "------- CLIENT REQUEST -------\n"
+ "------- END CLIENT REQUEST -------\n"
+ "------- END SERVER RESPONSE -------\n"
+ "------- SERVER RESPONSE -------\n"
+ "--------------------------------------------------------------\n"
+ "/Library/Caches/com.apple.xbs/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ "/private/var/tmp/usr/standalone/firmware/Savage/"
+ "/tmp/%@"
+ "/tmp/%@-from-server"
+ "00"
+ "0x"
+ "1.2"
+ ":"
+ "ApChipID"
+ "ApChipID: %@"
+ "ApECID"
+ "ApECID: %@"
+ "AppleBiometricServices"
+ "AppleKeyStore"
+ "C4"
+ "C5"
+ "C6"
+ "C7"
+ "CFDataCreate sik_digest failed"
+ "CFPropertyListCreateData failed\n"
+ "CFPropertyListCreateData failed : %@\n"
+ "Calling pearl patch loading."
+ "CameraH10 devices not supported"
+ "Command"
+ "Command = %@\n"
+ "Content Length -- empty \n"
+ "Content Length Empty"
+ "Content-Length"
+ "Content-Type"
+ "Could not create proxy settings, system default proxy will be used."
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n"
+ "Create UpdaterOptions successfully, value of ticket is: %@"
+ "Create xmlData failed, error: %@"
+ "Create xmlData failed."
+ "Creating savage updater ..."
+ "DataRef or responseDict is NULL."
+ "Device info dict is %@"
+ "Digest"
+ "Disabling SSL validation"
+ "Empty deviceInfoDict"
+ "Error is empty"
+ "ErrorCode"
+ "ErrorCode is String Type"
+ "ErrorMessage"
+ "ErrorMessage - %@"
+ "ErrorString : %@\n"
+ "Exiting parse_response : %d"
+ "Extracted patch digest: %@"
+ "FNvQ6lBvJIUcYBzQ8ggOUQ"
+ "Failed to allocate UpdaterOptions."
+ "Failed to create %s obj::error: %@"
+ "Failed to create FDR permission string"
+ "Failed to create connection options dictionary.\n"
+ "Failed to create max attempts\n"
+ "Failed to create timeout\n"
+ "Failed to enable single sign on"
+ "Failed to encode RIK keyBlob to base64 data"
+ "Failed to exec Savage Updater command: %@"
+ "Failed to exec SavageUpdater Command: %@:%@"
+ "Failed to find patch files"
+ "Failed to get Savage Serial Number"
+ "Failed to get Savage UID"
+ "Failed to get default AMAuthInstallRef"
+ "Failed to get manifest ticket"
+ "Failed to get pearl nonce with error %@"
+ "Failed to initialize personalization manager with error %@"
+ "Failed to load savage patch. Error: %@"
+ "Failed to pair pearl: %i, error: %@"
+ "Failed to power cycle sensor: %@"
+ "Failed to request FDR permission"
+ "Failed to set SEP nonce with error %d"
+ "Failed to set TATSU server URL with error %d"
+ "Failed to sign payload data"
+ "FirmwareData"
+ "Found patch files successfully"
+ "HSCGetPearlNonce"
+ "HSCSecurePairPearlWithProxy"
+ "HTTP Status == 200. OK\n"
+ "HTTP send error: %d\n"
+ "HorizonSeaCookieErrorDomain"
+ "IODeviceTree:/chosen"
+ "IOService:/IOResources/AppleKeyStore"
+ "Input argument req_dict is empty or NULL\n"
+ "Invalid Argument"
+ "Invalid Arguments"
+ "LE2kQ7U1iM32AmlhYvlagg"
+ "Library-MesaFactory"
+ "MesaFactoryC seacookie message handling."
+ "Not supported."
+ "Options"
+ "Output - Module Function = %@\n"
+ "POST"
+ "PairProjector"
+ "PairProjectorFinal"
+ "Payload = %@\n"
+ "Pearl Nonce Size: %d"
+ "Pearl Nonce: %@"
+ "PearlFactoryLib seacookie message handling."
+ "PersonalizedFirmwareRootPath"
+ "Processing Message  %@ --> %@"
+ "Protocol Version : %@"
+ "RePairingSessionKeyExchange"
+ "ReprovisionSensor"
+ "Request"
+ "Request Dictionary Creation failed\n"
+ "Request data is : %@\n"
+ "Resetting session\n"
+ "Response"
+ "Response Dictionary : %@\n"
+ "RestoreInternal"
+ "S4"
+ "S5"
+ "S6"
+ "SERVER RESPONSE is NULL\n"
+ "SIK"
+ "SIK : %@"
+ "Savage"
+ "Savage Serial Number: %@"
+ "Savage UID: %@"
+ "Savage,Ticket"
+ "SeaCookie server returned HTTP status: %ld\n"
+ "SeaCookiePairingOption"
+ "Seacookie Pairing URL: %@"
+ "Send request status: %d http status: %ld error: %@\n"
+ "SensorChipID"
+ "SensorChipID : %@"
+ "SensorChipID: %@"
+ "SensorNonce"
+ "SensorNonce : %@"
+ "SensorSN"
+ "SensorSN: %@"
+ "SensorSNUM"
+ "SensorSNUM: %@"
+ "SensorType"
+ "SensorType : %@"
+ "SensorUID"
+ "SensorUID: %@"
+ "SepNonce"
+ "SepNonce : %@"
+ "Server did not return session cookie"
+ "Server returned an "
+ "Session"
+ "Setting custom TATSU server URL: %@"
+ "Signature = %@\n"
+ "SpecVersion"
+ "TrustedAccessoryFactory seacookie message handling."
+ "UUID"
+ "Unable to create Error object\n"
+ "Unable to get Mesa Information"
+ "Unable to get Pearl Information"
+ "Unable to get pearl nonce"
+ "Unable to parse response data from SeaCookie server\n"
+ "Unable to receive Module Information\n"
+ "Unable to relay response to SEP and obtain information \n"
+ "Unable to send/receive data with SeaCookie server\n"
+ "Unable to validate tatsu ticket"
+ "Unknown SeaCookie type"
+ "Unknown callback type."
+ "Unknown camera type"
+ "Unprovisioned sensor"
+ "Update savage firmware successfully"
+ "Validate tatsu ticket succeeded."
+ "Version"
+ "X-Apple-SeaCookie-IP"
+ "XML datalen: %lu data is : %@\n"
+ "^{__CFString=}24@?0r*8Q16"
+ "_HSCGetMesaInfo"
+ "_HSCGetModuleInfo"
+ "_HSCGetPearlInfo"
+ "_HSCHandleMesaMessage"
+ "_HSCHandleMessage"
+ "_HSCHandleMessage Failed"
+ "_HSCHandleMessage returned : %d"
+ "_HSCHandlePearlMessage"
+ "_HSCHandlePearlMessage_block_invoke"
+ "_HSCPairProxy"
+ "_HSCSeaCookieHandler"
+ "_aks_operation"
+ "_merge_dict_cb"
+ "aks"
+ "aks-client-queue"
+ "aksStatus is %d"
+ "application/xml"
+ "appropriate command is not present"
+ "base64EncodedStringWithOptions:"
+ "callback"
+ "chipID: %u Size: %llu"
+ "could not create contentLengthStr\n"
+ "could not create httpRequest\n"
+ "createError"
+ "createRequestData"
+ "dataWithBytes:length:"
+ "der_key_validate"
+ "development-cert"
+ "enableSSO:"
+ "failed to open connection to %s\n"
+ "getApTicketForSeaCookiePairingWithOptions:pairingTicket:error:"
+ "getClientAuth"
+ "getDefaultAMAuthInstallRef"
+ "getSIKString"
+ "i24@?0r*8Q16"
+ "i28@?0i8r*12Q20"
+ "inData"
+ "initWithAuthInstallObj:"
+ "initWithBase64EncodedString:options:"
+ "inputData"
+ "inputData --> %@ inputSize --> %lu"
+ "isSSR"
+ "mesaInfo"
+ "mesaStatus: %d Size: %d"
+ "moduleStatus = %d reply[%lu] \n"
+ "numberWithInteger:"
+ "parseResponse"
+ "pearlInfo"
+ "pearlSeaCookieHandleMessage %d %p %zu %p %p\n"
+ "pearlSeaCookieHandleMessage, type=%d -> 0x%x\n"
+ "pearlSeaCookieHandleMessage, type=%d reply[%zu] %.*P\n"
+ "pearlStatus: %d Size: %d"
+ "performNextStage"
+ "powerCycleSensor:"
+ "queryInfo"
+ "requestData : %@ responseData : %@"
+ "responseDict : %@"
+ "responseDict NULL. Unable to parse Response\n"
+ "result : %d"
+ "result = %d\n"
+ "seaCookieHandleMessage %d %p %zu %p %p\n"
+ "seaCookieHandleMessage message[%zu] %.*P\n"
+ "seaCookieHandleMessage, type=%d -> 0x%x\n"
+ "seaCookieHandleMessage, type=%d reply[%zu] %.*P\n"
+ "sendRequestSync"
+ "shouldPersonalizeWithSSOByDefault"
+ "sign:keyBlob:"
+ "signature"
+ "sik_digest is NULL"
+ "sik_pub_key is NULL"
+ "sik_pub_key_len is 0"
+ "size == sizeof(state)"
+ "startPairing"
+ "unable to create a request \n"
+ "useProdMasterKey"
+ "xmlData : %@"
+ "xmlData is not CFDictionary type."

```
