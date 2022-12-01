Imports System

Module Program
    Sub Main(args As String())
        Dim input As String() = New String(13) {1000, 2000, 3000, "", 4000, "", 5000, 6000, "", 7000, 8000, 9000, "", 10000}
        Dim largest = 0
        Dim current
        Dim i
        Dim total = 0
        Dim length As Integer = input.Length
        If length = 0 Then Return
        For index As Integer = 0 To length - 1
            i = index
            current = input(i)
            If input(i) = "" Then
                If (total >= largest) Then
                    largest = total 'if larger than largest, make new largest
                    total = 0
                End If
            Else
                total += Convert.ToInt32(current)
            End If
        Next
        If (total >= largest) Then
            largest = total 'if larger than largest, make new largest
        End If
        Console.WriteLine(largest)
    End Sub
End Module
