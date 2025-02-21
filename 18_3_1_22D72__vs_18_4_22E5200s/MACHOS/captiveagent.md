## captiveagent

> `/usr/libexec/captiveagent`

```diff

-480.60.4.0.0
-  __TEXT.__text: 0x9d00
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x31c
-  __TEXT.__const: 0x15e
-  __TEXT.__cstring: 0x732
-  __TEXT.__oslogstring: 0xf04
-  __TEXT.__gcc_except_tab: 0x15c
-  __TEXT.__objc_methname: 0xecb
-  __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methtype: 0x759
-  __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x558
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x398
-  __DATA_CONST.__cfstring: 0x640
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+491.100.2.0.0
+  __TEXT.__text: 0x109b0
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_stubs: 0x15e0
+  __TEXT.__objc_methlist: 0xcb8
+  __TEXT.__const: 0x146
+  __TEXT.__gcc_except_tab: 0x394
+  __TEXT.__objc_methname: 0x1d0b
+  __TEXT.__oslogstring: 0x16bf
+  __TEXT.__cstring: 0x7ae
+  __TEXT.__objc_classname: 0xd1
+  __TEXT.__objc_methtype: 0xa05
+  __TEXT.__unwind_info: 0x448
+  __DATA_CONST.__auth_got: 0x588
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__cfstring: 0x8a0
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0xab0
-  __DATA.__objc_selrefs: 0x368
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x270
-  __DATA.__bss: 0x8
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA.__objc_const: 0x1948
+  __DATA.__objc_selrefs: 0x850
+  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x2f0
+  __DATA.__bss: 0x48
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 154
-  Symbols:   226
-  CStrings:  478
+  Functions: 311
+  Symbols:   238
+  CStrings:  714
 
Symbols:
+ _NSStringFromClass
+ _NSXMLParserErrorDomain
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$_NSXMLParser
+ __Block_object_dispose
+ _dispatch_after
+ _dispatch_once
+ _dispatch_time
+ _objc_enumerationMutation
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_setProperty_nonatomic_copy
- _CFHTTPMessageCopyHeaderFieldValue
- _CFHTTPMessageSetBody
- _CFRunLoopRemoveTimer
- _CFStringCreateWithFormat
CStrings:
+ "\x11\x15"
+ "\x12"
+ "#"
+ "#24@0:8@16"
+ "%@ 1st HTML/XML parsing completed"
+ "%@ HTML/XML parsing failed, %@"
+ "%@ WISPr XML parsing failed, %@"
+ "%@ XML parsing completed, WISPr dictionary: %@"
+ "%@ authentication poll request was responded with too big data"
+ "%@ authentication request was responded with too big data"
+ "%@ data task received data larger than 128KB"
+ "%@ data task received invalid response"
+ "%@ did not find required HTML element: [%@] in the parsed dictionary, stopping"
+ "%@ didCompleteWithError [%@]"
+ "%@ didEndElement: element:[%@]"
+ "%@ didReceiveChallenge [%@]"
+ "%@ didReceiveData [%@]"
+ "%@ didReceiveResponse [%@]"
+ "%@ didStartElement: element:[%@]"
+ "%@ failed to create HTML parser"
+ "%@ failed to extract parseable data from the received data"
+ "%@ found type [%@] for element: [%@], stopping"
+ "%@ foundCharacters:[%@]"
+ "%@ foundComment:[%@]"
+ "%@ handleTaskCompletion: parsing received data"
+ "%@ handleTaskCompletion: received redirect URL: [%@]"
+ "%@ handleTaskCompletion: reporting unknown state"
+ "%@ looking for HTML element: [%@] in the parsed dictionary"
+ "%@ parseErrorOccurred:[%@]"
+ "%@ parsed and expected values failed to match for required HTML elements"
+ "%@ parserDidEndDocument"
+ "%@ parserDidStartDocument"
+ "%@ probe data task received HTTP redirect response %s location header"
+ "%@ probe data task received response with a location header"
+ "%@ reached max limit of authentication poll with [%@]"
+ "%@ received authentication poll reply with \"Authentication Pending\" with delay: %@"
+ "%@ received authentication reply with \"Authentication Pending\" with delay: %@"
+ "%@ received authentication reply with \"Authentication Pending\" without %@"
+ "%@ received parse result %ld"
+ "%@ received parse result AuthPollReply"
+ "%@ received parse result AuthReply"
+ "%@ received parse result [%@]"
+ "%@ required WISPr AuthenticationPollReply element: [%@] was not found in the parsed dictionary, stopping"
+ "%@ required WISPr AuthenticationReply element: [%@] was not found in the parsed dictionary, stopping"
+ "%@ required element: [%@] was not found in the parsed dictionary, stopping"
+ "%@ starting authentication poll"
+ "%@ the session is invalidated"
+ "%@ the task was cancelled"
+ "%@ validationErrorOccurred:[%@]"
+ "%@ willPerformHTTPRedirection [%@]"
+ "%@ willPerformHTTPRedirection [%@]: received redirect %s HTTP body"
+ "%lu"
+ "&"
+ "&amp;"
+ "</WISPAccessGatewayParam>"
+ "</html>"
+ "<WISPAccessGatewayParam"
+ "<html"
+ "@\"NSData\"40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
+ "@\"NSMutableDictionary\""
+ "@\"NSMutableString\""
+ "@\"NSXMLParser\""
+ "@24@0:8q16"
+ "@32@0:8@16q24"
+ "@36@0:8@16B24#28"
+ "@40@0:8@16@24@32"
+ "BODY"
+ "CNCaptiveProber"
+ "CNCaptiveProber dealloced"
+ "CNHTMLParser"
+ "CNWISPrLoginHandler"
+ "CNWISPrLoginHandler dealloced"
+ "HEAD"
+ "HTML"
+ "NSXMLParserDelegate"
+ "T#,R,N,V_type"
+ "T@\"NSData\",C,N,V_receivedData"
+ "T@\"NSMutableDictionary\",&,N,V_htmlDictionary"
+ "T@\"NSMutableDictionary\",&,N,V_wisprDictionary"
+ "T@\"NSMutableString\",&,N,V_currentElementValue"
+ "T@\"NSString\",&,N,V_currentElementName"
+ "T@\"NSString\",C,N,V_wisprXMLDoc"
+ "T@\"NSString\",R,N,V_elementName"
+ "T@\"NSURL\",&,N,V_pollURL"
+ "T@\"NSURL\",&,N,V_redirectURL"
+ "T@\"NSURLSessionDataTask\",&,N,V_probeDataTask"
+ "T@\"NSXMLParser\",&,N,V_parser"
+ "TB,R,N,V_required"
+ "TB,V_foundHTML"
+ "TB,V_foundWISPr"
+ "TITLE"
+ "Ti,N,V_pollAttempts"
+ "Tq,N,V_purpose"
+ "WISPr login handler provided response: %@"
+ "_CNMarkupElement"
+ "_currentElementName"
+ "_currentElementValue"
+ "_elementName"
+ "_foundHTML"
+ "_foundWISPr"
+ "_handleAuthenticationChallenge:task:completionHandler:"
+ "_htmlDictionary"
+ "_parser"
+ "_pollAttempts"
+ "_pollURL"
+ "_probeDataTask"
+ "_purpose"
+ "_redirectURL"
+ "_required"
+ "_type"
+ "_wisprDictionary"
+ "_wisprXMLDoc"
+ "abortParsing"
+ "allKeys"
+ "appendString:"
+ "arrayWithObjects:count:"
+ "authReplyDictionary:"
+ "authentication poll request received %s response %{public}@ for %{public}@"
+ "authentication request received %s response %{public}@ for %{public}@"
+ "captive prober provided response result code: %u, response: %@"
+ "caseInsensitiveCompare:"
+ "configuration"
+ "containsAuthPollReplyElement:"
+ "containsAuthReplyElement:"
+ "containsHTMLElement:"
+ "containsObject:"
+ "containsRedirectElement:"
+ "containsString:"
+ "countByEnumeratingWithState:objects:count:"
+ "currentElementName"
+ "currentElementValue"
+ "data task received response with status code %lu"
+ "dictionaryWithDictionary:"
+ "elementName"
+ "enumerateObjectsUsingBlock:"
+ "expectedContentLength"
+ "extractHTMLDocData:"
+ "extractXMLDoc:"
+ "failure"
+ "foundHTML"
+ "foundRequiredAuthPollReplyElements"
+ "foundRequiredAuthReplyElements"
+ "foundRequiredNonCaptiveHTMLElements"
+ "foundRequiredRedirectElements"
+ "foundWISPr"
+ "handleAuthReply"
+ "handleAuthenticationPollReply:"
+ "handleAuthenticationReply:"
+ "handleTaskCompletion:"
+ "handleTaskFailure:"
+ "hasHTTPBody:"
+ "host"
+ "htmlDictionary"
+ "i"
+ "i16@0:8"
+ "initWithData:"
+ "initWithData:purpose:"
+ "initWithElementName:required:type:"
+ "initWithInteger:"
+ "intValue"
+ "integerValue"
+ "isAcceptableStatusCode:"
+ "localizedDescription"
+ "loginWithURL:data:"
+ "markupElementWithName:required:type:"
+ "not-captive"
+ "parse"
+ "parseReceivedData"
+ "parseReceivedData:"
+ "parseResultStr:"
+ "parseWithCompletionHandler:"
+ "parser"
+ "parser:didEndElement:namespaceURI:qualifiedName:"
+ "parser:didEndMappingPrefix:"
+ "parser:didStartElement:namespaceURI:qualifiedName:attributes:"
+ "parser:didStartMappingPrefix:toURI:"
+ "parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:"
+ "parser:foundCDATA:"
+ "parser:foundCharacters:"
+ "parser:foundComment:"
+ "parser:foundElementDeclarationWithName:model:"
+ "parser:foundExternalEntityDeclarationWithName:publicID:systemID:"
+ "parser:foundIgnorableWhitespace:"
+ "parser:foundInternalEntityDeclarationWithName:value:"
+ "parser:foundNotationDeclarationWithName:publicID:systemID:"
+ "parser:foundProcessingInstructionWithTarget:data:"
+ "parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:"
+ "parser:parseErrorOccurred:"
+ "parser:resolveExternalEntityName:systemID:"
+ "parser:validationErrorOccurred:"
+ "parserDidEndDocument:"
+ "parserDidStartDocument:"
+ "parserError"
+ "parserReadyData:"
+ "poll"
+ "pollAfter:"
+ "pollAttempts"
+ "pollURL"
+ "probeDataTask"
+ "purpose"
+ "q"
+ "q16@0:8"
+ "redirectDictionary:"
+ "redirectURL"
+ "required"
+ "response"
+ "scanLocation"
+ "scanUpToString:intoString:"
+ "setCharactersToBeSkipped:"
+ "setConnectionProxyDictionary:"
+ "setCurrentElementName:"
+ "setCurrentElementValue:"
+ "setDelegate:"
+ "setFoundHTML:"
+ "setFoundWISPr:"
+ "setHTTPBody:"
+ "setHTTPMethod:"
+ "setHtmlDictionary:"
+ "setParser:"
+ "setPollAttempts:"
+ "setPollURL:"
+ "setProbeDataTask:"
+ "setPurpose:"
+ "setRedirectURL:"
+ "setShouldProcessNamespaces:"
+ "setShouldResolveExternalEntities:"
+ "setWisprDictionary:"
+ "setWisprXMLDoc:"
+ "set_alternativeServicesStorage:"
+ "start:"
+ "startProbeTaskWithURL:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringByTrimmingCharactersInSet:"
+ "stringWithFormat:"
+ "supportedHTMLElements"
+ "supportedWISPrAuthPollReplyXMLElements"
+ "supportedWISPrAuthReplyXMLElements"
+ "supportedWISPrRedirectXMLElements"
+ "type"
+ "typeForAuthPollReplyElement:"
+ "typeForAuthReplyElement:"
+ "typeForRedirectElement:"
+ "unknown"
+ "v16@?0^{__CFDictionary=}8"
+ "v20@0:8B16"
+ "v20@0:8i16"
+ "v24@0:8@\"NSXMLParser\"16"
+ "v24@0:8q16"
+ "v24@?0q8@\"NSDictionary\"16"
+ "v32@0:8@\"NSXMLParser\"16@\"NSData\"24"
+ "v32@0:8@\"NSXMLParser\"16@\"NSError\"24"
+ "v32@0:8@\"NSXMLParser\"16@\"NSString\"24"
+ "v32@?0@\"_CNMarkupElement\"8Q16^B24"
+ "v40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
+ "v48@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@16@24@32@40"
+ "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48"
+ "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
+ "v56@0:8@16@24@32@40@48"
+ "whitespaceAndNewlineCharacterSet"
+ "wispr"
+ "wisprDictionary"
+ "wisprXMLDoc"
+ "with"
+ "without"
- "%d"
- "%ld redirect %@"
- "<unknown>"
- "Auth Notify..."
- "CFStringCreateWithFormat failed"
- "CFURLCreateWithString failed"
- "Delay of %d"
- "DetectedProxy"
- "Error"
- "Failed to retry probe"
- "HostnameError"
- "Intermediate"
- "Network Error: Failed to retry probe. Giving up after retrying %d times"
- "Network Error: Scheduling timer to try again in %.2f seconds. retryCount=%d"
- "NetworkError"
- "Proxy delay %d greater than max allowed: %d"
- "Result = %s (%d)"
- "Retrying probe. retryCount=%d"
- "ServerError"
- "Timeout"
- "Too many Authentication Poll Tries"
- "TooBig"
- "WISPr"
- "WISPr dict = %@"
- "http_client_auth_poll_start failed"
- "http_client_create_login_message failed"
- "http_parser_wispr_find_and_parse failed"
- "http_ref failed"
- "loginResultsURL is NULL"

```
