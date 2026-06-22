## WorkflowKit

> `FileSystem/System/Library/PrivateFrameworks/WorkflowKit.framework/Localizable.loctable`

```diff

 en.* List Style (ListStyle) = "* List Style"
 en.**Extensions**
 Apps installed on your device can expose models to Shortcuts, so you can tap into their broad world knowledge and domain expertise. You can enable extensions in Settings > Apple Intelligence & Siri. = "**Extensions**\nApps installed on your device can expose models to Shortcuts, so you can tap into their broad world knowledge and domain expertise. You can enable extensions in Settings \u003e Apple Intelligence \u0026 Siri."
+en.**Private Cloud Compute Models**
+Use large server-based models on Private Cloud Compute to handle complex requests while protecting your privacy.
+
+**On-Device Model**
+Use the on-device model to handle simple requests without the need for a network connection. = "**Private Cloud Compute Models**\nUse large server-based models on Private Cloud Compute to handle complex requests while protecting your privacy.\n\n**On-Device Model**\nUse the on-device model to handle simple requests without the need for a network connection."
 en.+ (WFMathOperation) = "+"
 en.,  = ", "
 en., (Parameter Placeholder) = ","

 en.Automatically runs this shortcut at the specified time of day. = "Automatically runs this shortcut at the specified time of day."
 en.Automatically runs this shortcut when Airplane Mode is turned on or off. = "Automatically runs this shortcut when Airplane Mode is turned on or off."
 en.Automatically runs this shortcut when CarPlay is connected or disconnected. = "Automatically runs this shortcut when CarPlay is connected or disconnected."
-en.Automatically runs this shortcut when a Low Power Mode is turned on or off. = "Automatically runs this shortcut when a Low Power Mode is turned on or off."
+en.Automatically runs this shortcut when Low Power Mode is turned on or off. = "Automatically runs this shortcut when Low Power Mode is turned on or off."
 en.Automatically runs this shortcut when a display is connected or disconnected. = "Automatically runs this shortcut when a display is connected or disconnected."
 en.Automatically runs this shortcut when a focus mode is turned on or off. = "Automatically runs this shortcut when a focus mode is turned on or off."
 en.Automatically runs this shortcut when a keyboard is connected or disconnected. = "Automatically runs this shortcut when a keyboard is connected or disconnected."

 en.Automatically runs this shortcut when you arrive at the specified location. = "Automatically runs this shortcut when you arrive at the specified location."
 en.Automatically runs this shortcut when you leave the specified location. = "Automatically runs this shortcut when you leave the specified location."
 en.Automatically runs this shortcut when you receive a notification from the specified app. = "Automatically runs this shortcut when you receive a notification from the specified app."
+en.Automation Input = "Automation Input"
 en.Automation was disabled because the folder exceeds maximum allowed size = "Automation was disabled because the folder exceeds maximum allowed size"
 en.Automation was disabled because the folder was moved to trash = "Automation was disabled because the folder was moved to trash"
 en.Average (WFStatisticsOperation) = "Average"

 en.If this option is enabled, and a URL is passed in, this action will fetch the title of the corresponding web page. (GetWebPageTitle) = "If this option is enabled, and a URL is passed in, this action will fetch the title of the corresponding web page."
 en.If this option is enabled, this action will get all the files inside of a folder, including its subfolders. (Recursive) = "If this option is enabled, this action will get all the files inside of a folder, including its subfolders."
 en.If you only see some but not all of your data in the results, make sure that “Allow Shortcuts to read data” is set to on in the Health app. = "If you only see some but not all of your data in the results, make sure that “Allow Shortcuts to read data” is set to on in the Health app."
+en.If you reconnect to any WLAN network within 3 minutes of being disconnected, this automation will run again. = "If you reconnect to any WLAN network within 3 minutes of being disconnected, this automation will run again."
 en.If you reconnect to any Wi-Fi network within 3 minutes of being disconnected, this automation will run again. = "If you reconnect to any Wi-Fi network within 3 minutes of being disconnected, this automation will run again."
 en.If you set the volume using a variable, use a number between 0 and 1 (for example, pass 0.5 for half volume). (WFVolume) = "If you set the volume using a variable, use a number between 0 and 1 (for example, pass 0.5 for half volume)."
 en.If you specify a variable, the contents of that variable will be included in the list. = "If you specify a variable, the contents of that variable will be included in the list."

 en.Payment Method (PaymentMethod) = "Payment Method"
 en.Percentage (WFImageResizeKey) = "Percentage"
 en.Percentage (WFImageResizePercentage) = "Percentage"
-en.Perception Description = "Perception Description"
 en.Perform the action “%@” in %@. = "Perform the action “%@” in %@."
 en.Performs a number operation on the input and returns the result. = "Performs a number operation on the input and returns the result."
 en.Performs the specified x-callback-url action. The x-success, x-cancel, and x-error parameters will be added automatically. = "Performs the specified x-callback-url action. The x-success, x-cancel, and x-error parameters will be added automatically."

 en.Response (WFStopAndRespondResponse) = "Response"
 en.Responses are automatically optimized for the actions they're passed into — for example, if the response is passed into the 'Repeat with Each' action, the model creates a list.
 
-To manually specify the model's output, select an output type using the 'Output' parameter.
-
-**Private Cloud Compute Models**
-Use large server-based models on Private Cloud Compute to handle complex requests while protecting your privacy.
-
-**On-Device Model**
-Use the on-device model to handle simple requests without the need for a network connection. = "Responses are automatically optimized for the actions they're passed into — for example, if the response is passed into the 'Repeat with Each' action, the model creates a list.\n\nTo manually specify the model's output, select an output type using the 'Output' parameter.\n\n**Private Cloud Compute Models**\nUse large server-based models on Private Cloud Compute to handle complex requests while protecting your privacy.\n\n**On-Device Model**\nUse the on-device model to handle simple requests without the need for a network connection."
+To manually specify the model's output, select an output type using the 'Output' parameter. = "Responses are automatically optimized for the actions they're passed into — for example, if the response is passed into the 'Repeat with Each' action, the model creates a list.\n\nTo manually specify the model's output, select an output type using the 'Output' parameter."
 en.Result (WFOutput) = "Result"
 en.Result (WFResponse) = "Result"
 en.Result = "Result"

 en.Trigger name: WLAN = "WLAN"
 en.Trigger name: Wi-Fi = "Wi-Fi"
 en.TriggerEnablementLabel = "Automation"
-en.TriggerNotifyLabel = "Notify When Run"
+en.TriggerNotifyLabel = "Notify"
+en.TriggerShowConfirmationLabel = "Confirm Before Run"
 en.Trim ${WFInputMedia} (Parameter Summary) = "Trim ${WFInputMedia}"
 en.Trim (TransformMethod) = "Trim"
 en.Trim Media (Action Name) = "Trim Media"

 en.is not exactly = "is not exactly"
 en.is not on = "is not on"
 en.is on = "is on"
+en.is on or after = "is on or after"
+en.is on or before = "is on or before"
 en.is shorter than = "is shorter than"
 en.is shorter than or equal to = "is shorter than or equal to"
 en.is smaller than = "is smaller than"

```
