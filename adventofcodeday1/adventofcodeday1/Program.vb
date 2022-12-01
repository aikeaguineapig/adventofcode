Imports System

Module Program
    Sub Main(args As String())
        Dim file As String = "../../../input.txt"
        Dim input As New ArrayList
        FileOpen(1, file, OpenMode.Input)
        Do While Not EOF(1)
            input.Add(LineInput(1))
        Loop
        FileClose(1)
        Dim largest = 0
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
                If (total >= largest) Then
                    largest = total 'if larger than largest, make new largest
                End If
                total = 0
            End If
        Next
        If (total >= largest) Then
            largest = total 'if larger than largest, make new largest
        End If
        Console.WriteLine(largest)
    End Sub
End Module
