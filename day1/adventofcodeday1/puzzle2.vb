Imports System

Module Program
    Sub puzzle2(args As String())
        Dim file As String = "../../../input.txt"
        Dim input As New ArrayList
        FileOpen(1, file, OpenMode.Input)
        Do While Not EOF(1)
            input.Add(LineInput(1))
        Loop
        FileClose(1)
        Dim largest1 = 0
        Dim largest2 = 0
        Dim largest3 = 0
        Dim current
        Dim i
        Dim total = 0
        Dim length As Integer = input.Count
        If length = 0 Then Return
        For index As Integer = 0 To length - 1
            i = index
            current = input(i)
            If IsNumeric(current) Then
                total += Convert.ToInt32(current)
            Else
                If (total > largest1) Then
                    largest2 = largest1
                    largest1 = total 'if larger than largest, make new largest
                Else
                    If (total > largest2) Then
                        largest3 = largest2
                        largest2 = total 'if larger than largest, make new largest
                    Else
                        If (total > largest3) Then
                            largest3 = total 'if larger than largest, make new largest
                        End If
                    End If
                End If
                total = 0
            End If
        Next
        If (total > largest1) Then
            largest1 = total 'if larger than largest, make new largest
        Else
            If (total > largest2) Then
                largest2 = total 'if larger than largest, make new largest
            End If
            If (total > largest3) Then
                largest3 = total 'if larger than largest, make new largest
            End If
        End If
        Console.WriteLine(largest1)
        Console.WriteLine(largest2)
        Console.WriteLine(largest3)
        Return
    End Sub
End Module
