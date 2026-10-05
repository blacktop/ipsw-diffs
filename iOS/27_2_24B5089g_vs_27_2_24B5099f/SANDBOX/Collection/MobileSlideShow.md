## MobileSlideShow

> Group: ⬆️ Updated

```diff

 				(global-name "com.apple.messages.critical-messaging")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+					(%entitlement-is-present "com.apple.developer.upi-device-validation")
 					(xpc-service-name ".viewservice")
 				)
 			)

 			(xpc-service-name "com.apple.imfoundation.IMRemoteURLConnectionAgent")
 			(xpc-service-name "com.apple.intents.intents-helper")
 			(xpc-service-name "com.apple.siri.context.service")
+			(xpc-service-name "com.apple.siri.orchestration.capabilities")
 			(xpc-service-name "com.apple.textkit.nsattributedstringagent")
 			(xpc-service-name "com.apple.tonelibraryd")
 		)

 				(global-name "com.apple.messages.critical-messaging")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+					(%entitlement-is-present "com.apple.developer.upi-device-validation")
 					(xpc-service-name ".viewservice")
 				)
 			)

 			(xpc-service-name "com.apple.imfoundation.IMRemoteURLConnectionAgent")
 			(xpc-service-name "com.apple.intents.intents-helper")
 			(xpc-service-name "com.apple.siri.context.service")
+			(xpc-service-name "com.apple.siri.orchestration.capabilities")
 			(xpc-service-name "com.apple.textkit.nsattributedstringagent")
 			(xpc-service-name "com.apple.tonelibraryd")
 		)

 				(global-name "com.apple.messages.critical-messaging")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+					(%entitlement-is-present "com.apple.developer.upi-device-validation")
 					(xpc-service-name ".viewservice")
 				)
 			)

 			(xpc-service-name "com.apple.imfoundation.IMRemoteURLConnectionAgent")
 			(xpc-service-name "com.apple.intents.intents-helper")
 			(xpc-service-name "com.apple.siri.context.service")
+			(xpc-service-name "com.apple.siri.orchestration.capabilities")
 			(xpc-service-name "com.apple.textkit.nsattributedstringagent")
 			(xpc-service-name "com.apple.tonelibraryd")
 		)
```
