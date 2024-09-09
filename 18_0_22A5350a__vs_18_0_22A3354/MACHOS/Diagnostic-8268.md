## Diagnostic-8268

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0xb5c
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x220
+  __TEXT.__text: 0x90b8
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0x4c0
   __TEXT.__objc_methlist: 0xbc
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x170
-  __TEXT.__oslogstring: 0xbb
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x1640
+  __TEXT.__oslogstring: 0x58a
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0x437
+  __TEXT.__objc_methname: 0x5b3
   __TEXT.__objc_methtype: 0x11b
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__cfstring: 0x1c0
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_classrefs: 0x10
+  __DATA_CONST.__objc_intobj: 0x108
   __DATA.__objc_const: 0x5e0
-  __DATA.__objc_selrefs: 0xd8
+  __DATA.__objc_selrefs: 0x160
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x184
+  __DATA.__common: 0x28
+  __DATA.__bss: 0x38
+  - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /usr/lib/libFDR.dylib

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15
-  Symbols:   46
-  CStrings:  121
+  Functions: 85
+  Symbols:   164
+  CStrings:  389
 
Symbols:
+ _ccder_blob_decode_sequence_tl
+ _ccder_blob_encode_tl
+ _IORegistryEntryFromPath
+ _CFDataCreate
+ _CFHTTPMessageCopyAllHeaderFields
+ _kAMSupportHttpOptionDisableSSLValidation
+ _kAMSupportHttpOptionTimeout
+ _kIOMainPortDefault
+ _AMSupportLogInternal
+ _OBJC_CLASS_$_CRPersonalizationManager
+ _memmove
+ _CFDictionaryGetTypeID
+ _CFNumberCreate
+ _IOServiceGetMatchingService
+ __NSConcreteStackBlock
+ ___osLogPearlLibTrace
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _AMSupportCreateSetFromCFIndexArray
+ _ccder_sizeof
+ _mach_task_self_
+ _memset_s
+ _ccsha384_di
+ _fprintf
+ _OBJC_CLASS_$_CRPreflightController
+ _CFDictionaryContainsKey
+ _CFStringCreateWithFormat
+ _AMSupportHttpCopyProxySettings
+ _CFDataGetBytes
+ _HSCSecureProvisionMesaWithUID
+ _IORegistryEntryCreateCFProperty
+ _ccder_blob_decode_len
+ _malloc
+ _AMAuthInstallApImg4SetSepNonce
+ _ccder_blob_decode_tl
+ _dispatch_once
+ _qsort
+ ___stdoutp
+ _kCFHTTPVersion1_1
+ _syslog
+ _CFStringAppend
+ _bzero
+ _kCFAllocatorDefault
+ _objc_release
+ _CFRelease
+ _CFPropertyListCreateData
+ _CFRetain
+ ___chkstk_darwin
+ _calloc
+ _kCFTypeDictionaryValueCallBacks
+ _memcmp
+ _CFDataCreateCopy
+ _ccder_blob_decode_range
+ _dispatch_queue_create
+ _kAMSupportHttpOptionMaxAttempts
+ _malloc_type_malloc
+ _OBJC_CLASS_$_NSNumber
+ _IOServiceClose
+ _pearlSeaCookieHandleMessage
+ _CFDictionaryGetValue
+ ___osLogPearlLib
+ __logHandler
+ _malloc_type_calloc
+ _memcpy
+ _AMFDRSealingMapGetFDRDataVersionForDevice
+ _IOObjectRelease
+ _CFDictionaryCreateCopy
+ _CFHTTPMessageCreateRequest
+ _AMSupportLogSetHandler
+ __os_log_default
+ _ccder_blob_decode_tag
+ _CFErrorCreate
+ _CFStringCreateMutable
+ _HSCGetMesaNonce
+ _OBJC_CLASS_$_NSFileManager
+ _CFDictionaryCreateMutable
+ _CFPropertyListCreateWithData
+ _IOServiceOpen
+ _kAMSupportHttpOptionValidResponses
+ _kCFErrorLocalizedDescriptionKey
+ _kCFNull
+ _kCFTypeDictionaryKeyCallBacks
+ _CFDataCreateWithBytesNoCopy
+ _CFDictionaryAddValue
+ _objc_release_x28
+ _AMSupportHttpSendSync
+ _CFStringGetTypeID
+ _IOConnectCallStructMethod
+ _dispatch_sync
+ _CFDataGetLength
+ _AMAuthInstallSetSigningServerURL
+ _kCFAllocatorMalloc
+ _OBJC_CLASS_$_NSString
+ ___stderrp
+ _kIOMasterPortDefault
+ _CFStringCompare
+ _CFHTTPMessageSetHeaderFieldValue
+ _CFDataGetBytePtr
+ _CFStringCreateMutableCopy
+ _IOServiceMatching
+ __NSConcreteGlobalBlock
+ _free
+ _kAMSupportHttpOptionSocksProxySettings
+ _AMSupportCopyHexStringFromData
+ _os_log_create
+ _CFUUIDCreate
+ _CFDataGetTypeID
+ _HSCSecureProvisionMesaWithUIDProxy
+ _OBJC_CLASS_$_NSMutableDictionary
+ _ccder_blob_encode_body
+ _AMSupportLogDumpMemory
+ _CFUUIDCreateString
+ _IOConnectCallMethod
+ _objc_retainBlock
+ _CFGetTypeID
+ _CFHTTPMessageSetBody
+ _ccdigest
+ _CFDictionarySetValue
CStrings:
+ "POST"
+ "ApECID: %!@(MISSING)"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-PearlFactory'!\n"
+ "Mesa Nonce Size: %!d(MISSING)"
+ "XML datalen: %!l(MISSING)u data is : %!@(MISSING)\n"
+ "No Error"
+ "xmlData is not CFDictionary type."
+ "numberWithInteger:"
+ "SensorSN"
+ "Session"
+ "_HSCHandlePearlMessage"
+ "could not create contentLengthStr\n"
+ "%!(BADPREC)%!s(MISSING)"
+ "AppleKeyStore"
+ "Payload = %!@(MISSING)\n"
+ "Setting custom tatsu server URL: %!@(MISSING)"
+ "seaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "--------------------------------------------------------------\n"
+ "Failed to set TATSU server URL with error %!d(MISSING)"
+ "Invalid Arguments"
+ "Request Dictionary Creation failed\n"
+ "seaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || reply"
+ "Exiting parse_response : %!d(MISSING)"
+ "_HSCGetModuleInfo"
+ "could not create httpRequest\n"
+ "getClientAuth"
+ "HTTP Status == 200. OK\n"
+ "application/xml"
+ "mesaSensorSerialNumber"
+ "buffer"
+ "seaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "S7"
+ "SensorNonce"
+ "i28@?0i8r*12Q20"
+ "getModuleSerialNumber %!p(MISSING) %!p(MISSING)\n"
+ "HSCGetMesaNonce"
+ "Processing Message  %!@(MISSING) --> %!@(MISSING)"
+ "SensorType"
+ "result : %!d(MISSING)"
+ "size == sizeof(state)"
+ "%!l(MISSING)u"
+ "Failed to create max attempts\n"
+ "IOService:/IOResources/AppleKeyStore"
+ "Invalid Argument"
+ "callback"
+ "getApTicketForSeaCookiePairingWithOptions:pairingTicket:error:"
+ "Unable to get mesa nonce"
+ "_HSCGetMesaInfo"
+ "com.apple.BiometricKit"
+ "i"
+ "xmlData : %!@(MISSING)"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize"
+ "HorizonSeaCookieErrorDomain"
+ "Unable to parse response data from SeaCookie server\n"
+ "_HSCSeaCookieHandler"
+ "initWithBytes:length:encoding:"
+ "_HSCHandleMessage returned : %!d(MISSING)"
+ "_aks_operation"
+ "Content-Length"
+ "Library-MesaFactory"
+ "_HSCGetPearlInfo"
+ "failed to open connection to %!s(MISSING)\n"
+ "/tmp/%!@(MISSING)"
+ "CFPropertyListCreateData failed\n"
+ "responseDict : %!@(MISSING)"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply"
+ "isSSR"
+ "SensorType : %!@(MISSING)"
+ "SepNonce"
+ "TrustedAccessoryFactory seacookie message handling."
+ "Unable to create Error object\n"
+ "_HSCHandleMessage"
+ "------- END CLIENT REQUEST -------\n"
+ "SensorChipID: %!@(MISSING)"
+ "_HSCHandleMessage Failed"
+ "bufferSize"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) aks connection failed%!s(MISSING)\n"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || message"
+ "Mesa sensor serial number: %!@(MISSING)"
+ "Unable to relay response to SEP and obtain information \n"
+ "Unknown SeaCookie type"
+ "responseDict NULL. Unable to parse Response\n"
+ "sign:keyBlob:"
+ "------- CLIENT REQUEST -------\n"
+ "0x"
+ "SepNonce : %!@(MISSING)"
+ "SIK"
+ "development-cert"
+ "00"
+ "Failed to set SEP nonce with error %!d(MISSING)"
+ "Input argument req_dict is empty or NULL\n"
+ "Library-PearlFactory"
+ "Mesa Module serial number: %!@(MISSING)"
+ "Request"
+ "getModuleSerialNumber -> %!{(MISSING)errno}d\n"
+ "shouldPersonalizeWithSSOByDefault"
+ "sik_digest is NULL"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize"
+ "CFDataCreate sik_digest failed"
+ "DataRef or responseDict is NULL."
+ "Send request status: %!d(MISSING) http status: %!l(MISSING)d error: %!@(MISSING)\n"
+ "getInnermostNSError:"
+ "AssertMacros: %!s(MISSING) (value = 0x%!l(MISSING)x), %!s(MISSING) file: %!s(MISSING), line: %!d(MISSING)\n\n"
+ "SensorChipID : %!@(MISSING)"
+ "Validate tatsu ticket succeeded."
+ "code"
+ "%!X(MISSING)"
+ "C6"
+ "S5"
+ "SensorChipID"
+ "C7"
+ "Unable to send/receive data with SeaCookie server\n"
+ "Unknown callback type."
+ "aks"
+ "getSensorSerialNumber %!p(MISSING) %!p(MISSING)\n"
+ "/tmp/%!@(MISSING)-from-server"
+ "Command = %!@(MISSING)\n"
+ "Server did not return session cookie"
+ "mesaInfo"
+ "aksStatus is %!d(MISSING)"
+ "err == 0 "
+ "requestData : %!@(MISSING) responseData : %!@(MISSING)"
+ "%!@(MISSING)\n"
+ "der_key_validate"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "ReprovisionSensor"
+ "Unable to receive Module Information\n"
+ "mesaModuleSerialNumber"
+ "sendRequestSync"
+ "-[MesaPairer start]"
+ "SessionKeyExch"
+ "_HSCHandleMesaMessage"
+ "chipID: %!u(MISSING) Size: %!l(MISSING)lu"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 1%!s(MISSING)\n"
+ "appropriate command is not present"
+ "v8@?0"
+ "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
+ "1.2"
+ "Protocol Version : %!@(MISSING)"
+ "Request data is : %!@(MISSING)\n"
+ "SensorUID: %!@(MISSING)"
+ "signature"
+ "PairSensor"
+ "Response"
+ "Unable to get Pearl Information"
+ "getSensorProvisioningState -> %!{(MISSING)errno}d %!d(MISSING)\n"
+ "_merge_dict_cb"
+ "getDefaultAMAuthInstallRef"
+ "/Library/Caches/com.apple.xbs/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ ":"
+ "ApChipID"
+ "ApplePearlSEPDriver"
+ "Command"
+ "CFPropertyListCreateData failed : %!@(MISSING)\n"
+ "mesaStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "parseResponse"
+ "ErrorCode"
+ "Mesa Nonce: %!@(MISSING)"
+ "Unable to get current mesa provisioning state"
+ "mesaSensorPreviousState"
+ "------- END SERVER RESPONSE -------\n"
+ "C5"
+ "SensorSNUM: %!@(MISSING)"
+ "aks-client-queue"
+ "inputData"
+ "pearlSeaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "ApChipID: %!@(MISSING)"
+ "AppleBiometricServices"
+ "C4"
+ "Unable to get mesa serial number"
+ "result = %!d(MISSING)\n"
+ "------- SERVER RESPONSE -------\n"
+ "ErrorCode is String Type"
+ "Resetting session\n"
+ "localizedDescription"
+ "ErrorMessage - %!@(MISSING)"
+ "RePairingSessionKeyExchange"
+ "Response Dictionary : %!@(MISSING)\n"
+ "_HSCPairProxy"
+ "numberWithUnsignedInt:"
+ "X-Apple-SeaCookie-IP"
+ "^{__CFString=}24@?0r*8Q16"
+ "dataWithBytes:length:"
+ "initWithAuthInstallObj:"
+ "unable to create a request \n"
+ "Could not create proxy settings, system default proxy will be used."
+ "Failed to create timeout\n"
+ "_HSCHandlePearlMessage_block_invoke"
+ "absoluteString"
+ "inData"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) fail%!s(MISSING)\n"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || replySize"
+ "Signature = %!@(MISSING)\n"
+ "createRequestData"
+ "enableSSO:"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 2%!s(MISSING)\n"
+ "Failed to get default AMAuthInstallRef"
+ "SensorNonce : %!@(MISSING)"
+ "SpecVersion"
+ "%!d(MISSING)"
+ "MesaFactoryC seacookie message handling."
+ "SensorUID"
+ "Unable to get Mesa Information"
+ "inputData --> %!@(MISSING) inputSize --> %!l(MISSING)u"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "Content Length -- empty \n"
+ "Error is empty"
+ "Failed to create connection options dictionary.\n"
+ "Not supported."
+ "Output - Module Function = %!@(MISSING)\n"
+ "S6"
+ "seaCookieHandleMessage message[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "\terrorCode: "
+ "Content-Type"
+ "ErrorMessage"
+ "Failed to get mesa nonce with error %!@(MISSING)"
+ "HSCSecureProvisionMesaWithUIDProxy"
+ "sik_pub_key_len is 0"
+ "\terrorString: "
+ "Failed to initialize personalization manager with error %!@(MISSING)"
+ "getSensorProvisioningState %!p(MISSING)\n"
+ "HTTP send error: %!d(MISSING)\n"
+ "SERVER RESPONSE is NULL\n"
+ "SIK : %!@(MISSING)"
+ "Calling pearl patch loading."
+ "Disabling SSL validation"
+ "Unable to validate tatsu ticket"
+ "moduleStatus = %!d(MISSING) reply[%!l(MISSING)u] \n"
+ "ApECID"
+ "sik_pub_key is NULL"
+ "Content Length Empty"
+ "service"
+ "*replySize >= outData->dataSize"
+ "Create xmlData failed."
+ "Fail to provision mesa: %!i(MISSING) error: %!@(MISSING)"
+ "startPairing"
+ "stringWithFormat:"
+ "PearlFactoryLib seacookie message handling."
+ "SeaCookie server returned HTTP status: %!l(MISSING)d\n"
+ "cmd"
+ "pearlStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "useProdMasterKey"
+ "base64EncodedStringWithOptions:"
+ "getSensorSerialNumber -> %!{(MISSING)errno}d\n"
+ "Failed to enable single sign on"
+ "SensorSN: %!@(MISSING)"
+ "mesaSensorProvisioningState"
+ "Unable to get mesa provisioning state"
+ "Version"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message"
+ "Create xmlData failed, error: %!@(MISSING)"
+ "ErrorString : %!@(MISSING)\n"
+ "IODeviceTree:/chosen"
+ "createError"
+ "*bufferSize"
+ "Server returned an "
+ "UUID"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n"
+ "SensorSNUM"
+ "getSIKString"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || messageLength"
+ "pearlInfo"

```
