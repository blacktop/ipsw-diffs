## Diagnostic-8268

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268`

```diff

 645.62.1.0.0
-  __TEXT.__text: 0x3cc0
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x3c0
+  __TEXT.__text: 0xb9fc
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x496
-  __TEXT.__cstring: 0x400
+  __TEXT.__const: 0xc0
+  __TEXT.__oslogstring: 0x8b8
+  __TEXT.__cstring: 0x1845
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0x5e5
+  __TEXT.__objc_methname: 0x75f
   __TEXT.__objc_methtype: 0x159
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x80
-  __DATA_CONST.__cfstring: 0x3c0
+  __TEXT.__unwind_info: 0x148
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__cfstring: 0xee0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_classrefs: 0x8
+  __DATA_CONST.__objc_intobj: 0x108
   __DATA.__objc_const: 0x670
-  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_selrefs: 0x1e0
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc4
-  __DATA.__bss: 0x18
-  __DATA.__common: 0x18
+  __DATA.__data: 0x184
+  __DATA.__bss: 0x48
+  __DATA.__common: 0x28
+  - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 46
-  Symbols:   85
-  CStrings:  209
+  Functions: 112
+  Symbols:   184
+  CStrings:  467
 
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
+ _CFStringGetTypeID
+ _CFUUIDCreate
+ _CFUUIDCreateString
+ _HSCGetMesaNonce
+ _HSCSecureProvisionMesaWithUID
+ _HSCSecureProvisionMesaWithUIDProxy
+ _IOConnectCallMethod
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ _OBJC_CLASS_$_CRPersonalizationManager
+ _OBJC_CLASS_$_CRPreflightController
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSNumber
+ __NSConcreteStackBlock
+ ___chkstk_darwin
+ ___osLogPearlLib
+ ___osLogPearlLibTrace
+ ___stderrp
+ ___stdoutp
+ __logHandler
+ _bzero
+ _calloc
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
+ _fprintf
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
+ _kIOMainPortDefault
+ _malloc
+ _malloc_type_calloc
+ _memcmp
+ _memcpy
+ _memset_s
+ _objc_release
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
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || message"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || messageLength"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || reply"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || replySize"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize"
+ "*bufferSize"
+ "*replySize >= outData->dataSize"
+ "------- CLIENT REQUEST -------\n"
+ "------- END CLIENT REQUEST -------\n"
+ "------- END SERVER RESPONSE -------\n"
+ "------- SERVER RESPONSE -------\n"
+ "--------------------------------------------------------------\n"
+ "-[MesaPairer start]"
+ "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
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
+ "AppleKeyStore"
+ "ApplePearlSEPDriver"
+ "C4"
+ "C5"
+ "C6"
+ "C7"
+ "CFDataCreate sik_digest failed"
+ "CFPropertyListCreateData failed\n"
+ "CFPropertyListCreateData failed : %@\n"
+ "Calling pearl patch loading."
+ "Command"
+ "Command = %@\n"
+ "Content Length -- empty \n"
+ "Content Length Empty"
+ "Content-Length"
+ "Content-Type"
+ "Could not create proxy settings, system default proxy will be used."
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-PearlFactory'!\n"
+ "Create xmlData failed, error: %@"
+ "Create xmlData failed."
+ "DataRef or responseDict is NULL."
+ "Disabling SSL validation"
+ "Error is empty"
+ "ErrorCode"
+ "ErrorCode is String Type"
+ "ErrorMessage"
+ "ErrorMessage - %@"
+ "ErrorString : %@\n"
+ "Exiting parse_response : %d"
+ "Fail to provision mesa: %i error: %@"
+ "Failed to create connection options dictionary.\n"
+ "Failed to create max attempts\n"
+ "Failed to create timeout\n"
+ "Failed to enable single sign on"
+ "Failed to get default AMAuthInstallRef"
+ "Failed to get mesa nonce with error %@"
+ "Failed to initialize personalization manager with error %@"
+ "Failed to set SEP nonce with error %d"
+ "Failed to set TATSU server URL with error %d"
+ "HSCGetMesaNonce"
+ "HSCSecureProvisionMesaWithUIDProxy"
+ "HTTP Status == 200. OK\n"
+ "HTTP send error: %d\n"
+ "HorizonSeaCookieErrorDomain"
+ "IODeviceTree:/chosen"
+ "IOService:/IOResources/AppleKeyStore"
+ "Input argument req_dict is empty or NULL\n"
+ "Invalid Argument"
+ "Invalid Arguments"
+ "Library-PearlFactory"
+ "Mesa Module serial number: %@"
+ "Mesa Nonce Size: %d"
+ "Mesa Nonce: %@"
+ "Mesa sensor serial number: %@"
+ "MesaFactoryC seacookie message handling."
+ "No Error"
+ "Not supported."
+ "Output - Module Function = %@\n"
+ "POST"
+ "PairSensor"
+ "Payload = %@\n"
+ "PearlFactoryLib seacookie message handling."
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
+ "S5"
+ "S6"
+ "S7"
+ "SERVER RESPONSE is NULL\n"
+ "SIK"
+ "SIK : %@"
+ "SeaCookie server returned HTTP status: %ld\n"
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
+ "SessionKeyExch"
+ "Setting custom tatsu server URL: %@"
+ "Signature = %@\n"
+ "SpecVersion"
+ "TrustedAccessoryFactory seacookie message handling."
+ "UUID"
+ "Unable to create Error object\n"
+ "Unable to get Mesa Information"
+ "Unable to get Pearl Information"
+ "Unable to get current mesa provisioning state"
+ "Unable to get mesa nonce"
+ "Unable to get mesa provisioning state"
+ "Unable to get mesa serial number"
+ "Unable to parse response data from SeaCookie server\n"
+ "Unable to receive Module Information\n"
+ "Unable to relay response to SEP and obtain information \n"
+ "Unable to send/receive data with SeaCookie server\n"
+ "Unable to validate tatsu ticket"
+ "Unknown SeaCookie type"
+ "Unknown callback type."
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
+ "absoluteString"
+ "aks"
+ "aks-client-queue"
+ "aksStatus is %d"
+ "application/xml"
+ "appropriate command is not present"
+ "base64EncodedStringWithOptions:"
+ "buffer"
+ "bufferSize"
+ "callback"
+ "chipID: %u Size: %llu"
+ "code"
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
+ "getInnermostNSError:"
+ "getModuleSerialNumber %p %p\n"
+ "getModuleSerialNumber -> %{errno}d\n"
+ "getSIKString"
+ "getSensorSerialNumber %p %p\n"
+ "getSensorSerialNumber -> %{errno}d\n"
+ "getSensorSerialNumber, retry: %d\n"
+ "i"
+ "i28@?0i8r*12Q20"
+ "inData"
+ "initWithAuthInstallObj:"
+ "initWithBytes:length:encoding:"
+ "inputData"
+ "inputData --> %@ inputSize --> %lu"
+ "isSSR"
+ "localizedDescription"
+ "mesaInfo"
+ "mesaModuleSerialNumber"
+ "mesaSensorPhysicalPresenceState"
+ "mesaSensorPreviousPhysicalPresenceState"
+ "mesaSensorPreviousState"
+ "mesaSensorProvisioningState"
+ "mesaSensorSerialNumber"
+ "mesaStatus: %d Size: %d"
+ "moduleStatus = %d reply[%lu] \n"
+ "numberWithBool:"
+ "numberWithInteger:"
+ "numberWithUnsignedInt:"
+ "parseResponse"
+ "pearlInfo"
+ "pearlSeaCookieHandleMessage %d %p %zu %p %p\n"
+ "pearlSeaCookieHandleMessage, type=%d -> 0x%x\n"
+ "pearlSeaCookieHandleMessage, type=%d reply[%zu] %.*P\n"
+ "pearlStatus: %d Size: %d"
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
+ "startPairing"
+ "unable to create a request \n"
+ "useProdMasterKey"
+ "xmlData : %@"
+ "xmlData is not CFDictionary type."

```
