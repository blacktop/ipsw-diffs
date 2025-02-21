## CFNetwork

> `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`

```diff

-3826.400.120.0.0
-  __TEXT.__text: 0x270894
-  __TEXT.__auth_stubs: 0x5560
+3826.500.62.2.1
+  __TEXT.__text: 0x26f820
+  __TEXT.__auth_stubs: 0x5630
   __TEXT.__delay_stubs: 0x7e8
   __TEXT.__delay_helper: 0x1728
-  __TEXT.__objc_methlist: 0x8e48
-  __TEXT.__const: 0xc9bcc
-  __TEXT.__gcc_except_tab: 0x15100
-  __TEXT.__cstring: 0x18da1
-  __TEXT.__oslogstring: 0xf807
+  __TEXT.__objc_methlist: 0x9c34
+  __TEXT.__const: 0xc9bfc
+  __TEXT.__cstring: 0x18e91
+  __TEXT.__gcc_except_tab: 0x15304
+  __TEXT.__oslogstring: 0xf7e5
   __TEXT.__dof_CFNetwork: 0xf3b
-  __TEXT.__unwind_info: 0xbe50
-  __TEXT.__objc_classname: 0x1514
-  __TEXT.__objc_methname: 0x17a18
-  __TEXT.__objc_methtype: 0x6ce5
-  __TEXT.__objc_stubs: 0xe680
-  __DATA_CONST.__got: 0xc38
-  __DATA_CONST.__const: 0x9390
-  __DATA_CONST.__objc_classlist: 0x4d8
-  __DATA_CONST.__objc_catlist: 0x10
+  __TEXT.__unwind_info: 0xbd48
+  __TEXT.__objc_classname: 0x1561
+  __TEXT.__objc_methname: 0x17cd2
+  __TEXT.__objc_methtype: 0x6d9e
+  __TEXT.__objc_stubs: 0xe800
+  __DATA_CONST.__got: 0xc30
+  __DATA_CONST.__const: 0x9428
+  __DATA_CONST.__objc_classlist: 0x4e8
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b60
+  __DATA_CONST.__objc_selrefs: 0x4c30
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x3e0
+  __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x2c38
+  __AUTH_CONST.__auth_got: 0x2ca0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x137a0
-  __AUTH_CONST.__cfstring: 0xf2e0
-  __AUTH_CONST.__objc_const: 0x15600
+  __AUTH_CONST.__const: 0x13848
+  __AUTH_CONST.__cfstring: 0xf400
+  __AUTH_CONST.__objc_const: 0x14300
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1630
+  __AUTH.__objc_data: 0x1680
   __AUTH.__data: 0x2f8
   __AUTH.__cfstring_CFN: 0x7cb0
-  __DATA.__objc_ivar: 0x1394
+  __DATA.__objc_ivar: 0x13bc
   __DATA.__data: 0x11a8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0xd50
-  __DATA_DIRTY.__objc_data: 0x1a40
+  __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__data: 0x1b0
   __DATA_DIRTY.__bss: 0xac8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12870
-  Symbols:   15028
-  CStrings:  9387
+  Functions: 12828
+  Symbols:   15096
+  CStrings:  9423
 
Symbols:
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$__NSURLSessionBackgroundTaskOverrides
+ _OBJC_METACLASS_$__NSURLSessionBackgroundTaskOverrides
+ _dyld_image_path_containing_address
+ _nw_array_apply
+ _nw_storage_copy_shared
+ _nw_storage_create_ephemeral
+ _nw_storage_create_persistent
+ _nw_storage_delete_all_data
+ _nw_storage_delete_all_data_for_registrable_domain
+ _nw_storage_delete_alt_svc
+ _nw_storage_lookup_all_origins_with_alt_svc
+ _nw_storage_lookup_all_origins_with_dns_cache
+ _nw_storage_lookup_all_origins_with_http_early_data_state
+ _nw_storage_lookup_alt_svc
+ _nw_storage_store_alt_svc
+ _sec_protocol_options_set_pqtls_mode
- _SANDBOX_CHECK_NO_REPORT
- _SANDBOX_CHECK_POSIX_WRITEABLE
- _sandbox_check_by_audit_token
CStrings:
+ "/.nofollow/"
+ "@\"_NSHTTPAlternativeServicesStorageSqlite\""
+ "AppSSO chose not to manage url"
+ "AppSSOProtocol Cannot Handle Task"
+ "B24@?0Q8@\"NSObject<OS_nw_object>\"16"
+ "BackgroundSession <%{public}@> didFinishDownloadingToURL received nil location"
+ "CREATE TABLE IF NOT EXISTS alt_services (\t\tpartition text NOT NULL,\t\thost text NOT NULL,\t\talternateHost text NOT NULL,\t\tport int NOT NULL,\t\talternatePort int NOT NULL,\t\ttype int NOT NULL,\t\tcreation_time int,\t\texpires_time int,\t\tUNIQUE(partition, host, port, type)\t\t);"
+ "Default Session Classes"
+ "Embrace.framework"
+ "Finished Merging Classes"
+ "Only supported on background sessions"
+ "ProxySession <%{public}@> didFinishDownloadingToURL received nil location"
+ "Skipping AppSSOProtocol"
+ "T@\"NSURL\",R,N,V_path"
+ "T@,R,V_underlyingStorage"
+ "TB,V_forceEnablePQTLS"
+ "TB,V_systemClientOfPrivateAccessTokens"
+ "T^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}{os_unfair_lock_s=I}CC},R,D"
+ "T^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}{os_unfair_lock_s=I}CC},V__cf_resp_data"
+ "Ti,V__allowsCellularAccess"
+ "Ti,V__allowsConstrainedNetworkAccess"
+ "Ti,V__allowsExpensiveNetworkAccess"
+ "Ti,V__requiresPowerPluggedIn"
+ "Ti,V_requiresPowerPluggedIn"
+ "^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}{os_unfair_lock_s=I}CC}"
+ "^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}{os_unfair_lock_s=I}CC}16@0:8"
+ "_NSHTTPAlternativeServicesStorageSqlite"
+ "_NSURLSessionBackgroundTaskOverrides"
+ "__allowsCellularAccess"
+ "__allowsConstrainedNetworkAccess"
+ "__allowsExpensiveNetworkAccess"
+ "__requiresPowerPluggedIn"
+ "_applyBackgroundTaskOverrides:"
+ "_explicitlySetRequiresDNSSECValidation"
+ "_fileMovedForResumption"
+ "_forceEnablePQTLS"
+ "_inMemory"
+ "_oldStorage"
+ "_systemClientOfPrivateAccessTokens"
+ "_underlyingStorage"
+ "allowsCellularAccess=%d allowsExpensiveNetworkAccess=%d allowsConstrainedNetworkAccess=%d requiresPowerPluggedIn=%d"
+ "applyOverrides:forTaskWithIdentifier:"
+ "bundleRecordForCurrentProcess"
+ "developerType"
+ "nw_loader_third_party_apps"
+ "requiresPowerPluggedIn"
+ "setRequiresPowerPluggedIn:"
+ "setSystemClient:"
+ "set_allowsCellularAccess:"
+ "set_allowsExpensiveNetworkAccess:"
+ "set_forceEnablePQTLS:"
+ "set_systemClientOfPrivateAccessTokens:"
+ "underlyingStorage"
+ "useKeychain"
+ "v16@?0@\"NSObject<OS_nw_array>\"8"
+ "v24@0:8^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}{os_unfair_lock_s=I}CC}16"
+ "v28@?0c8@\"NSObject<OS_nw_endpoint>\"12d20"
+ "v32@0:8@\"_NSURLSessionBackgroundTaskOverrides\"16Q24"
+ "{URLResponse=\"_vptr$CoreLoggable\"^^?\"fURL\"^{__CFURL}\"fMIMEType\"^{__CFString}\"fTextEncodingName\"^{__CFString}\"fExpectedContentLength\"q\"fExpiration\"d\"fCreationTime\"d\"fDownloadAssessment\"^{__CFDictionary}\"fSSLCertContext\"^{__CFDictionary}\"fRecommendedPolicy\"i\"fPeerAddress\"^{__CFData}\"fHTTP\"^{HTTPResponse}\"fLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"fConnectionDidFallback\"C\"fConnectionIsCellular\"C}"
+ "\x95&C3\x1cC"
- "(buf[0] & 0xC0) == 0x40"
- "B52@0:8i16{?=[8I]}20"
- "CREATE TABLE IF NOT EXISTS alt_services (        partition text NOT NULL,        host text NOT NULL,        alternateHost text NOT NULL,        port int NOT NULL,        alternatePort int NOT NULL,        type int NOT NULL,        creation_time int,        expires_time int,        UNIQUE(partition, host, port, type)        );"
- "GMT"
- "HTTPServiceEntriesWithRegistrableDomain:"
- "SELECT * from alt_services WHERE host LIKE ('%' || ?) OR partition LIKE ('%' || ?)"
- "TB,V_canSuspendLocked"
- "T^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}CC},R,D"
- "T^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}CC},V__cf_resp_data"
- "UT"
- "^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}CC}"
- "^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}CC}16@0:8"
- "_canSuspendLocked"
- "_isSafeDirectoryForDownloads:withToken:"
- "_isSafeFileForBackgroundUploadForMe"
- "_onqueue_createConnectionCache"
- "deleteExpiredEntriesStmt"
- "file-write-data"
- "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
- "lsqpack_enc_decoder_in"
- "ma"
- "sandbox_check_by_audit_token() returned %d for operation file-read-data for pid %d, errno %d"
- "sandbox_check_by_audit_token() returned %d for operation file-write-data for pid %d, errno %d"
- "trimDbStmt"
- "v24@0:8^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}CC}16"
- "{URLResponse=\"_vptr$CoreLoggable\"^^?\"fURL\"^{__CFURL}\"fMIMEType\"^{__CFString}\"fTextEncodingName\"^{__CFString}\"fExpectedContentLength\"q\"fExpiration\"d\"fCreationTime\"d\"fDownloadAssessment\"^{__CFDictionary}\"fSSLCertContext\"^{__CFDictionary}\"fRecommendedPolicy\"i\"fPeerAddress\"^{__CFData}\"fHTTP\"^{HTTPResponse}\"fConnectionDidFallback\"C\"fConnectionIsCellular\"C}"
- "\x85&C3\x1cC"

```
