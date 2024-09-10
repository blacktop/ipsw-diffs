## Diagnostic-8340

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0x31e0
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x580
+  __TEXT.__text: 0xb3a8
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0x1c4
-  __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x41c
-  __TEXT.__oslogstring: 0x4d9
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x1824
+  __TEXT.__oslogstring: 0xaa4
   __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x89d
+  __TEXT.__objc_methname: 0x9ca
   __TEXT.__objc_methtype: 0x147
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x3a0
+  __TEXT.__gcc_except_tab: 0x2b4
+  __TEXT.__unwind_info: 0x178
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__cfstring: 0xf60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x198
   __DATA.__objc_const: 0x7a0
-  __DATA.__objc_selrefs: 0x220
+  __DATA.__objc_selrefs: 0x280
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
-  Functions: 57
-  Symbols:   90
-  CStrings:  250
+  Functions: 140
+  Symbols:   197
+  CStrings:  519
 
Symbols:
+ _kCFAllocatorMalloc
+ _CFErrorCreate
+ _memcpy
+ _SavageUpdaterExecCommand
+ _kAMSupportHttpOptionValidResponses
+ _AMSupportHttpCopyProxySettings
+ _CFDataCreateWithBytesNoCopy
+ _CFStringCompare
+ _CFStringCreateMutableCopy
+ _bzero
+ _kCFTypeDictionaryKeyCallBacks
+ _memcmp
+ _objc_autoreleasePoolPop
+ _CFDictionaryGetValue
+ _CFDictionarySetValue
+ _MGCopyAnswer
+ ___stdoutp
+ _AMFDRSealingMapGetFDRDataVersionForDevice
+ _OBJC_CLASS_$_CRPreflightController
+ _SavageUpdaterCreate
+ _kCFBooleanTrue
+ _CFDictionaryCreateMutable
+ _pearlSeaCookieHandleMessage
+ _CFDataGetTypeID
+ _objc_release_x26
+ _qsort
+ __logHandler
+ _objc_autoreleasePoolPush
+ _CFDataGetLength
+ _HSCSecurePairPearlWithProxy
+ _CFHTTPMessageSetBody
+ _CFPropertyListCreateData
+ __Unwind_Resume
+ _ccder_blob_decode_sequence_tl
+ _ccder_sizeof
+ _malloc_type_malloc
+ _CFStringCreateMutable
+ _CFUUIDCreate
+ _kAMSupportHttpOptionDisableSSLValidation
+ _AMAuthInstallSetSigningServerURL
+ _AMSupportLogDumpMemory
+ _IORegistryEntryFromPath
+ _kCFBooleanFalse
+ _CFDictionaryCreateCopy
+ _ccder_blob_decode_tag
+ _dispatch_queue_create
+ _CFHTTPMessageCreateRequest
+ _CFStringAppend
+ _OBJC_CLASS_$_CRPersonalizationManager
+ _AMSupportHttpSendSync
+ _CFDictionaryContainsKey
+ _kCFHTTPVersion1_1
+ _kAMSupportHttpOptionMaxAttempts
+ _CFDataGetBytes
+ _CFHTTPMessageCopyAllHeaderFields
+ ___chkstk_darwin
+ _ccder_blob_decode_len
+ _CFStringCreateWithFormat
+ _kCFNull
+ _CFDataCreateCopy
+ __Block_object_dispose
+ _HSCGetPearlNonce
+ _CFDataCreate
+ _CFPropertyListCreateWithData
+ _ccder_blob_decode_range
+ _IORegistryEntryCreateCFProperty
+ _dispatch_sync
+ _kCFTypeDictionaryValueCallBacks
+ _OBJC_CLASS_$_NSNumber
+ _SavageUpdaterIsDone
+ _objc_retainBlock
+ _ccsha384_di
+ _AMSupportLogInternal
+ _CFDataGetBytePtr
+ _CFDictionaryGetTypeID
+ _CFHTTPMessageSetHeaderFieldValue
+ _CFRetain
+ _ccder_blob_encode_tl
+ _kAMSupportHttpOptionSocksProxySettings
+ _kCFErrorLocalizedDescriptionKey
+ _AMSupportLogSetHandler
+ _HSCSecurePairPearl
+ _malloc
+ _objc_release_x10
+ _CFRelease
+ __NSConcreteStackBlock
+ _objc_retain
+ _CFStringGetTypeID
+ _ccdigest
+ _CFStringGetCStringPtr
+ _memset_s
+ _syslog
+ _AMSupportCreateSetFromCFIndexArray
+ _CFDictionaryAddValue
+ _CFGetTypeID
+ _ccder_blob_encode_body
+ _kAMSupportHttpOptionTimeout
+ _AMAuthInstallApImg4SetSepNonce
+ _AMSupportCopyHexStringFromData
+ _CFNumberCreate
+ _ccder_blob_decode_tl
+ _CFURLCreateWithString
+ _CFUUIDCreateString
+ _IOConnectCallMethod
+ ___objc_personality_v0
+ _malloc_type_calloc
+ _objc_release_x9
CStrings:
+ "Content-Length"
+ "getClientAuth"
+ "parseResponse"
+ "Found patch files successfully"
+ "createError"
+ "Validate tatsu ticket succeeded."
+ "_HSCHandleMesaMessage"
+ "Digest"
+ "ErrorCode"
+ "HSCSecurePairPearlWithProxy"
+ "Savage Serial Number: %!@(MISSING)"
+ "RePairingSessionKeyExchange"
+ "appropriate command is not present"
+ "%!s(MISSING): %!s(MISSING)"
+ "Creating savage updater ..."
+ "_HSCHandleMessage returned : %!d(MISSING)"
+ "Request data is : %!@(MISSING)\n"
+ "getApTicketForSeaCookiePairingWithOptions:pairingTicket:error:"
+ "getSIKString"
+ "SIK"
+ "enableSSO:"
+ ":"
+ "Protocol Version : %!@(MISSING)"
+ "S4"
+ "ErrorCode is String Type"
+ "IODeviceTree:/chosen"
+ "responseDict NULL. Unable to parse Response\n"
+ "Failed to allocate UpdaterOptions."
+ "UUID"
+ "could not create contentLengthStr\n"
+ "result : %!d(MISSING)"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize"
+ "CFPropertyListCreateData failed : %!@(MISSING)\n"
+ "Failed to find patch files"
+ "inputData --> %!@(MISSING) inputSize --> %!l(MISSING)u"
+ "\terrorCode: "
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || message"
+ "C4"
+ "^{__CFString=}24@?0r*8Q16"
+ "SensorType : %!@(MISSING)"
+ "aks-client-queue"
+ "createRequestData"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) fail%!s(MISSING)\n"
+ "CFPropertyListCreateData failed\n"
+ "PairProjector"
+ "IOService:/IOResources/AppleKeyStore"
+ "1.2"
+ "Unable to create Error object\n"
+ "base64EncodedStringWithOptions:"
+ "Invalid Argument"
+ "SensorSN: %!@(MISSING)"
+ "isSSR"
+ "SensorSNUM"
+ "Server returned an "
+ "Failed to load savage patch. Error: %!@(MISSING)"
+ "i24@?0r*8Q16"
+ "der_key_validate"
+ "*replySize >= outData->dataSize"
+ "XML datalen: %!l(MISSING)u data is : %!@(MISSING)\n"
+ "/private/var/tmp/usr/standalone/firmware/Savage/"
+ "0x"
+ "Unable to get pearl nonce"
+ "Device info dict is %!@(MISSING)"
+ "--------------------------------------------------------------\n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) aks connection failed%!s(MISSING)\n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 1%!s(MISSING)\n"
+ "Request Dictionary Creation failed\n"
+ "Unable to receive Module Information\n"
+ "C6"
+ "Command = %!@(MISSING)\n"
+ "Content Length Empty"
+ "Not supported."
+ "C5"
+ "Unable to validate tatsu ticket"
+ "responseDict : %!@(MISSING)"
+ "PersonalizedFirmwareRootPath"
+ "HTTP Status == 200. OK\n"
+ "Unable to send/receive data with SeaCookie server\n"
+ "/Library/Caches/com.apple.xbs/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ "Failed to set SEP nonce with error %!d(MISSING)"
+ "Seacookie Pairing URL: %!@(MISSING)"
+ "\terrorString: "
+ "HSCGetPearlNonce"
+ "SepNonce"
+ "AppleKeyStore"
+ "_HSCSeaCookieHandler"
+ "sign:keyBlob:"
+ "Options"
+ "TrustedAccessoryFactory seacookie message handling."
+ "SensorChipID"
+ "%!l(MISSING)u"
+ "_HSCHandleMessage"
+ "S5"
+ "Failed to create %!s(MISSING) obj::error: %!@(MISSING)"
+ "Failed to create connection options dictionary.\n"
+ "SensorChipID : %!@(MISSING)"
+ "Exiting parse_response : %!d(MISSING)"
+ "LE2kQ7U1iM32AmlhYvlagg"
+ "SensorNonce : %!@(MISSING)"
+ "SepNonce : %!@(MISSING)"
+ "Pearl Nonce: %!@(MISSING)"
+ "00"
+ "ErrorMessage"
+ "development-cert"
+ "Failed to create FDR permission string"
+ "_HSCGetModuleInfo"
+ "mesaInfo"
+ "_HSCHandlePearlMessage"
+ "Failed to enable single sign on"
+ "SIK : %!@(MISSING)"
+ "SensorSNUM: %!@(MISSING)"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "Error is empty"
+ "signature"
+ "%!(BADPREC)%!s(MISSING)"
+ "Failed to get default AMAuthInstallRef"
+ "could not create httpRequest\n"
+ "mesaStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "queryInfo"
+ "Failed to request FDR permission"
+ "PairProjectorFinal"
+ "numberWithInteger:"
+ "sik_pub_key_len is 0"
+ "Savage UID: %!@(MISSING)"
+ "aksStatus is %!d(MISSING)"
+ "HorizonSeaCookieErrorDomain"
+ "Unable to parse response data from SeaCookie server\n"
+ "_HSCHandleMessage Failed"
+ "ApChipID"
+ "POST"
+ "callback"
+ "Content-Type"
+ "Failed to create timeout\n"
+ "Failed to power cycle sensor: %!@(MISSING)"
+ "PearlFactoryLib seacookie message handling."
+ "seaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "Create xmlData failed, error: %!@(MISSING)"
+ "Disabling SSL validation"
+ "Extracted patch digest: %!@(MISSING)"
+ "AppleBiometricServices"
+ "Empty deviceInfoDict"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message"
+ "Failed to sign payload data"
+ "Response Dictionary : %!@(MISSING)\n"
+ "ApECID: %!@(MISSING)"
+ "SensorUID"
+ "SensorNonce"
+ "size == sizeof(state)"
+ "SensorUID: %!@(MISSING)"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply"
+ "RestoreInternal"
+ "Savage,Ticket"
+ "aks"
+ "%!d(MISSING)"
+ "Could not create proxy settings, system default proxy will be used."
+ "Failed to get manifest ticket"
+ "SpecVersion"
+ "ApChipID: %!@(MISSING)"
+ "Content Length -- empty \n"
+ "Failed to encode RIK keyBlob to base64 data"
+ "Library-MesaFactory"
+ "Signature = %!@(MISSING)\n"
+ "ApECID"
+ "FirmwareData"
+ "%!X(MISSING)"
+ "CFDataCreate sik_digest failed"
+ "CameraH10 devices not supported"
+ "Resetting session\n"
+ "moduleStatus = %!d(MISSING) reply[%!l(MISSING)u] \n"
+ "Failed to get Savage UID"
+ "Server did not return session cookie"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || reply"
+ "------- END CLIENT REQUEST -------\n"
+ "FNvQ6lBvJIUcYBzQ8ggOUQ"
+ "Failed to create max attempts\n"
+ "seaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "Unknown SeaCookie type"
+ "Failed to get Savage Serial Number"
+ "Pearl Nonce Size: %!d(MISSING)"
+ "requestData : %!@(MISSING) responseData : %!@(MISSING)"
+ "_aks_operation"
+ "performNextStage"
+ "shouldPersonalizeWithSSOByDefault"
+ "Unknown camera type"
+ "seaCookieHandleMessage message[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "ErrorString : %!@(MISSING)\n"
+ "Failed to get pearl nonce with error %!@(MISSING)"
+ "Unprovisioned sensor"
+ "initWithAuthInstallObj:"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || messageLength"
+ "ReprovisionSensor"
+ "Request"
+ "SensorChipID: %!@(MISSING)"
+ "_HSCHandlePearlMessage_block_invoke"
+ "SensorType"
+ "powerCycleSensor:"
+ "seaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "Processing Message  %!@(MISSING) --> %!@(MISSING)"
+ "Session"
+ "Create xmlData failed."
+ "ErrorMessage - %!@(MISSING)"
+ "/tmp/%!@(MISSING)"
+ "/tmp/%!@(MISSING)-from-server"
+ "pearlSeaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "xmlData is not CFDictionary type."
+ "Calling pearl patch loading."
+ "Command"
+ "Input argument req_dict is empty or NULL\n"
+ "Unable to get Pearl Information"
+ "C7"
+ "Savage"
+ "_HSCGetPearlInfo"
+ "initWithBase64EncodedString:options:"
+ "%!@(MISSING)\n"
+ "MesaFactoryC seacookie message handling."
+ "Failed to exec SavageUpdater Command: %!@(MISSING):%!@(MISSING)"
+ "Unable to get Mesa Information"
+ "application/xml"
+ "i28@?0i8r*12Q20"
+ "sik_pub_key is NULL"
+ "startPairing"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize"
+ "Invalid Arguments"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n"
+ "Setting custom TATSU server URL: %!@(MISSING)"
+ "X-Apple-SeaCookie-IP"
+ "result = %!d(MISSING)\n"
+ "Failed to set TATSU server URL with error %!d(MISSING)"
+ "SeaCookie server returned HTTP status: %!l(MISSING)d\n"
+ "pearlStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "DataRef or responseDict is NULL."
+ "Failed to initialize personalization manager with error %!@(MISSING)"
+ "HTTP send error: %!d(MISSING)\n"
+ "inData"
+ "------- CLIENT REQUEST -------\n"
+ "Output - Module Function = %!@(MISSING)\n"
+ "Unknown callback type."
+ "------- SERVER RESPONSE -------\n"
+ "useProdMasterKey"
+ "Send request status: %!d(MISSING) http status: %!l(MISSING)d error: %!@(MISSING)\n"
+ "Unable to relay response to SEP and obtain information \n"
+ "_merge_dict_cb"
+ "xmlData : %!@(MISSING)"
+ "S6"
+ "dataWithBytes:length:"
+ "pearlInfo"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "chipID: %!u(MISSING) Size: %!l(MISSING)lu"
+ "failed to open connection to %!s(MISSING)\n"
+ "Failed to pair pearl: %!i(MISSING), error: %!@(MISSING)"
+ "Version"
+ "Payload = %!@(MISSING)\n"
+ "getDefaultAMAuthInstallRef"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 2%!s(MISSING)\n"
+ "Response"
+ "SensorSN"
+ "SERVER RESPONSE is NULL\n"
+ "_HSCPairProxy"
+ "sendRequestSync"
+ "unable to create a request \n"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || replySize"
+ "------- END SERVER RESPONSE -------\n"
+ "Create UpdaterOptions successfully, value of ticket is: %!@(MISSING)"
+ "Update savage firmware successfully"
+ "inputData"
+ "sik_digest is NULL"
+ "Failed to exec Savage Updater command: %!@(MISSING)"
+ "SeaCookiePairingOption"
+ "_HSCGetMesaInfo"

```
